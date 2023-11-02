# Social Media API Service

RESTful API for a social media platform. The API allows users to create profiles, follow other users, create and retrieve posts, manage likes and comments, and perform basic social media actions.


### Features:

* Admin panel: /admin/
* Documentation is located at: </api/doc/swagger/>, </api/doc/redoc/>
* Creating users and posts
* JWT authentication for users
* Ability to add comments to posts
* Ability to follow/unfollow users
* Ability to like/unlike posts and comments


## How to launch locally:

1. Clone the repository:

   ```
   git clone https://github.com/PodorogaNatalia/social-media-api
   ```

2. Navigate to the project directory:

   ```
   cd social_media_api
   ```

3. Create and activate a virtual environment:

   ```
   python -m venv venv
   
   source venv/bin/activate # For Mac OS/Linux
   
   venv\Scripts\activate  # For Windows
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Create .env file and define environmental variables following .env.sample


6. Install PostgreSQL and create a data base


7. Run the database migrations:

   ```
   python manage.py migrate
   ```

8. Run the development server:

   ```
   python manage.py runserver
   ```
   

## How to launch with docker:

1. Clone the repository:

   ```
   git clone https://github.com/PodorogaNatalia/social-media-api
   ```
   
2. Create .env file and define environmental variables following .env.sample


3. Install Docker on your machine.

   
4. Run command:

   ```
   docker-compose up --build
   ```
   
5. You should use such localhost for you app: ```127.0.0.1:8000```


## Service has next endpoints:
   ```
   "blog" : 
                "http://127.0.0.1:8000/api/blog/posts/"
                "http://127.0.0.1:8000/api/blog/posts/create/"
                "http://127.0.0.1:8000/api/blog/posts/{id}/"
                "http://127.0.0.1:8000/api/blog/posts/{id}/like_unlike/"
                "http://127.0.0.1:8000/api/blog/posts/{post_id}/comments/"
                "http://127.0.0.1:8000/api/blog/posts/{post_id}/comments/add/"
                "http://127.0.0.1:8000/api/blog/posts/{post_id}/comments/{id}/"
                "http://127.0.0.1:8000/api/blog/posts/{post_id}/comments/{id}/like_unlike/"
                
   "user" : 
                   "http://127.0.0.1:8000/api/user/register/"
                   "http://127.0.0.1:8000/api/user/{id}/"
                   "http://127.0.0.1:8000/api/user/{id}/followers/"
                   "http://127.0.0.1:8000/api/user/{id}/following/"
                   "http://127.0.0.1:8000/api/user/{id}/liked_posts/"
                   "http://127.0.0.1:8000/api/user/follow_unfollow/"
                   "http://127.0.0.1:8000/api/user/token/"
                   "http://127.0.0.1:8000/api/user/token/refresh/"
                   "http://127.0.0.1:8000/api/user/token/verify/"
   "documentation": 
                   "http://127.0.0.1:8000/api/swagger/"
                   "http://127.0.0.1:8000/api/redoc/"
   ```

## How to access

Create superuser:

   ```
   python manage.py createsuperuser
   ```

Also, you can create ordinary user at such endpoint:

   ```
   "http://127.0.0.1:8000/api/user/register/"
   ```

To work with token use such endpoints:

   ```
   "http://127.0.0.1:8000/api/user/token/" - to get access and refresh token
   "http://127.0.0.1:8000/api/user/token/refresh/" - to refresh access token
   "http://127.0.0.1:8000/api/user/token/verify/" - to verify access token
   ```

Add Token in api urls in Headers as follows:

   ```
   key: Authorization
   value: Bearer @token
   ```
