from datetime import date
from django.shortcuts import render

# Create your views here.
all_posts = [
    {
      "title": "Making a post post",
      "description": "this is the description of the post post that is created here",
      "slug": "making-a-post-post",
      "date" : date(2017,7,21),
      "imagePath":"a.jpg"

    },
    {
      "title": "Another post post",
      "description": "Hi, there can your read this description, it will take less than a two minute",
      "slug": "another-post-two-min-read",
      "date" : date(2017,7,20),
      "imagePath":"b.jpg"
    },
    {
        "title": "Created by myself",
        "description": "With the help of Maxmillian, I've created this post post project",
        "slug": "created-by-myself",
        "date" : date(2017,7,19),
        "imagePath":"c.jpg" 
    },
    {"title": "Making a post post",
        "description": "this is the description of the post post that is created here",
        "slug": "making-a-post-post",
        "date" : date(2017,7,18),
        "imagePath":"d.jpg" 
    },
    { 
      "title": "Another post post",
      "description": "Hi, there can your read this description, it will take less than a two minute",
      "slug": "another-post-two-min-read-6",
      "date" : date(2017,7,17),
        "imagePath":"a.jpg" 
    },
    {
      "title": "Created by myself",
      "description": "With the help of Maxmillian, I've created this post post project",
      "slug": "created-by-myself-1",
      "date" : date(2017,7,16),
        "imagePath":"b.jpg" 
    },
    { "title": "Making a post post",
      "description": "this is the description of the post post that is created here",
      "slug": "making-a-post-post-1",
      "date" : date(2017,7,15),
        "imagePath":"c.jpg" 
    },
    {
      "title": "Another post post",
      "description": "Hi, there can your read this description, it will take less than a two minute",
      "slug": "another-post-two-min-read",
      "date" : date(2017,7,14),
        "imagePath":"d.jpg" 
    },
    {
      "title": "Created by myself",
      "description": "With the help of Maxmillian, I've created this post post project",
      "slug": "created-by-myself-2",
      "date" : date(2017,7,13),
        "imagePath":"a.jpg" 
    },
    {
      "title": "Making a post post",
      "description": "this is the description of the post post that is created here",
      "slug": "making-a-post-post-2",
      "date" : date(2017,7,12),
        "imagePath":"b.jpg" 
    },
    {
      "title": "Another post post",
      "description": "Hi, there can your read this description, it will take less than a two minute",
      "slug": "another-post-two-min-read-2",
      "date" : date(2017,7,11),
        "imagePath":"c.jpg" 
    },
    { 
      "title": "Created by myself",
      "description": "With the help of Maxmillian, I've created this post post project",
      "slug": "created-by-myself-3",
      "date" : date(2017,7,10),
        "imagePath":"d.jpg" 
    },
    { 
      "title": "Making a post post",
      "description": "this is the description of the post post that is created here",
      "slug": "making-a-post-post-3",
      "date" : date(2017,7,9),
        "imagePath":"a.jpg" 
    },
    {
      "title": "Another post post",
      "description": "Hi, there can your read this description, it will take less than a two minute",
      "slug": "another-post-two-min-read-3",
      "date" : date(2017,7,8),
        "imagePath":"b.jpg" 
    },
    {
      "title": "Created by myself",
      "description": "With the help of Maxmillian, I've created this post post project",
      "slug": "created-by-myself-4",
      "date" : date(2017,7,8),
        "imagePath":"c.jpg" 
    },
    { "title": "Making a post post",
      "description": "this is the description of the post post that is created here",
      "slug": "making-a-post-post-4",
      "date" : date(2017,7,7),
        "imagePath":"d.jpg" 
    },
    { 
      "title": "Another post post",
      "description": "Hi, there can your read this description, it will take less than a two minute",
      "slug": "another-post-two-min-read-4",
      "date" : date(2017,7,6),
        "imagePath":"a.jpg" 
    },
    { 
      "title": "Created by myself",
      "description": "With the help of Maxmillian, I've created this post post project",
      "slug": "created-by-myself-5",
      "date" : date(2017,7,5),
      "imagePath":"b.jpg" 
    },
    {
      "title": "Making a post post",
      "description": "this is the description of the post post that is created here",
      "slug": "making-a-post-post-5",
      "date" : date(2017,7,4),
      "imagePath":"c.jpg" 
    },
    {
      "title": "Another post post",
      "description": "Hi, there can your read this description, it will take less than a two minute",
      "slug": "another-post-two-min-read-5",
      "date" : date(2017,7,3),
      "imagePath":"d.jpg" 
    },
    {
      "title": "Created by myself",
      "description": "With the help of Maxmillian, I've created this post post project",
      "slug": "created-by-myself-6",
      "date" : date(2017,7,2),
      "imagePath":"a.jpg" 
    },
]


def get_key(post):
  return post['date']

def index(request):
  sorted_posts = sorted(all_posts,key=get_key)
  latest_posts = sorted_posts[-3:]
  print(latest_posts)
  return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/posts.html", {"posts": all_posts})


def post_details(request, post_slug):
    postFound = next(post for post in all_posts if post["slug"] == post_slug)
    if postFound is not None:
        return render(request, "blog/post_details.html", {"post": postFound})
    else:
        return render(request, "404.html")
    endif
