from rest_framework import serializers

from blog.models import Comment, Post


class CommentListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="email"
    )
    like_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "author", "content", "like_count", "created_time"]


class CommentDetailSerializer(serializers.ModelSerializer):
    likes = serializers.SlugRelatedField(many=True, read_only=True, slug_field="email")

    class Meta:
        model = Comment
        fields = ["id", "content", "likes"]


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SlugRelatedField(many=True, read_only=True, slug_field="email")
    author = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="email"
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "content",
            "likes",
            "created_time",
            "image",
        ]


class PostCreateSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "image"]


class PostListSerializer(PostSerializer):
    comments = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="content"
    )
    author = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="email"
    )
    like_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "like_count",
            "created_time",
            "comments",
            "image",
        ]
