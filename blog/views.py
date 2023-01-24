from django.shortcuts import render

# Create your views here.
posts =[
  {"title":"Making a blog post", "description":"this is the description of the blog post that is created here","slug":"making-a-blog-post"},
  {"title":"Another blog post", "description":"Hi, there can your read this description, it will take less than a two minute","slug":"another-post-two-min-read"},
  {"title":"Created by myself", "description":"With the help of Maxmillian, I've created this blog post project","slug":"created-by-myself"},
  {"title":"Making a blog post", "description":"this is the description of the blog post that is created here","slug":"making-a-blog-post"},
  {"title":"Another blog post", "description":"Hi, there can your read this description, it will take less than a two minute","slug":"another-post-two-min-read-6"},
  {"title":"Created by myself", "description":"With the help of Maxmillian, I've created this blog post project","slug":"created-by-myself-1"},
  {"title":"Making a blog post", "description":"this is the description of the blog post that is created here","slug":"making-a-blog-post-1"},
  {"title":"Another blog post", "description":"Hi, there can your read this description, it will take less than a two minute","slug":"another-post-two-min-read"},
  {"title":"Created by myself", "description":"With the help of Maxmillian, I've created this blog post project","slug":"created-by-myself-2"},
  {"title":"Making a blog post", "description":"this is the description of the blog post that is created here","slug":"making-a-blog-post-2"},
  {"title":"Another blog post", "description":"Hi, there can your read this description, it will take less than a two minute","slug":"another-post-two-min-read-2"},
  {"title":"Created by myself", "description":"With the help of Maxmillian, I've created this blog post project","slug":"created-by-myself-3"},
  {"title":"Making a blog post", "description":"this is the description of the blog post that is created here","slug":"making-a-blog-post-3"},
  {"title":"Another blog post", "description":"Hi, there can your read this description, it will take less than a two minute","slug":"another-post-two-min-read-3"},
  {"title":"Created by myself", "description":"With the help of Maxmillian, I've created this blog post project","slug":"created-by-myself-4"},
  {"title":"Making a blog post", "description":"this is the description of the blog post that is created here","slug":"making-a-blog-post-4"},
  {"title":"Another blog post", "description":"Hi, there can your read this description, it will take less than a two minute","slug":"another-post-two-min-read-4"},
  {"title":"Created by myself", "description":"With the help of Maxmillian, I've created this blog post project","slug":"created-by-myself-5"},
  {"title":"Making a blog post", "description":"this is the description of the blog post that is created here","slug":"making-a-blog-post-5"},
  {"title":"Another blog post", "description":"Hi, there can your read this description, it will take less than a two minute","slug":"another-post-two-min-read-5"},
  {"title":"Created by myself", "description":"With the help of Maxmillian, I've created this blog post project","slug":"created-by-myself-6"},
]

def index(request):
  return render(request,"blog/index.html",{"posts":posts})

