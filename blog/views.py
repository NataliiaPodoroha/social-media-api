from django.db.models import Count
from django.http import HttpResponseRedirect
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from blog.models import Post, Comment
from blog.serializers import (
    PostSerializer,
    PostCreateSerializer,
    PostListSerializer,
    CommentDetailSerializer,
    CommentListSerializer,
)
from user.permissions import IsPostOwnerOrReadOnly


class Pagination(PageNumberPagination):
    page_size = 5
    max_page_size = 100


class PostListView(generics.ListAPIView):
    queryset = (
        Post.objects.prefetch_related("likes", "comments")
        .select_related("author")
        .annotate(like_count=Count("likes"))
        .order_by("-created_time")
    )
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PostListSerializer
    pagination_class = Pagination


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.validated_data["author"] = self.request.user
        serializer.save()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.select_related("author").prefetch_related("likes")
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsPostOwnerOrReadOnly,)
    serializer_class = PostSerializer


class CommentListView(generics.ListAPIView):
    queryset = (
        Comment.objects.select_related("author", "post")
        .prefetch_related("likes")
        .annotate(like_count=Count("likes"))
        .order_by("-created_time")
    )
    serializer_class = CommentListSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination

    def get_queryset(self):
        queryset = self.queryset
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        return queryset.filter(post=post)


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentDetailSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.validated_data["author"] = self.request.user
        serializer.validated_data["post_id"] = self.kwargs.get("post_id")
        serializer.save()


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentDetailSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsPostOwnerOrReadOnly,)

    def get_queryset(self):
        queryset = Comment.objects.select_related("author", "post")
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))

        return queryset.filter(post=post)


class LikeUnlikePostView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse("blog:posts-detail", args=[str(pk)]))


class LikeUnlikeCommentView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def post(self, request, post_id, pk):
        comment = get_object_or_404(Comment, id=pk)
        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)
        return HttpResponseRedirect(
            reverse("blog:comment-list", args=[str(post_id)]),
        )
