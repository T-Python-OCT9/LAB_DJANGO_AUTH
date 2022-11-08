from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def add_post(request : HttpRequest):
    user : User = request.user

    if not (user.is_authenticated and user.has_perm("blogApp.add_post")):
        return redirect("accounts:login_user")

    if request.method == "POST":
        new_post = Post(user = request.user, title=request.POST["title"], content = request.POST["content"], publish_date=request.POST["publish_date"], is_published = request.POST["is_published"], post_type=request.POST["post_type"] , image=request.FILES["image"])
        new_post.save()


    return render(request, "blogApp/add_post.html", {"Post" : Post})



def list_posts(request: HttpRequest):
    
    
    if "search" in request.GET:
        posts = Post.objects.filter(title__contains=request.GET["search"])
    else:
        posts = Post.objects.all()

    
    #posts = Post.objects.all().order_by("-publish_date") #to order by date
    #posts = Post.objects.filter(is_published=False) #to filter by exact
    #posts = Post.objects.filter(title__contains = "aims") #to filter using postfix __contains
    return render(request, "blogApp/view_posts.html", {"posts" : posts})



def post_detail(request : HttpRequest, post_id : int):

    try:
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post = post)
    except:
        return render(request , "blogApp/not_found.html")

    return render(request, "blogApp/post_detail.html", {"post" : post, "comments" : comments})


#update post
#if you want to use a decorator to check for login
@login_required(login_url="/account/login/")
def update_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "blogApp/not_found.html")

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.publish_date = request.POST["publish_date"]
        post.is_published = request.POST["is_published"]
        post.save()

        return redirect("blogApp:list_posts")

    post.publish_date = post.publish_date.isoformat("T", "hours").replace("+", ":")
    return render(request, "blogApp/update_post.html", {"post" : post})


#delete post
def delete_post(request: HttpRequest, post_id:int):

    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(request , "blogApp/not_found.html")

    post.delete()

    return redirect("blogApp:list_posts")




def add_comment(request: HttpRequest, post_id:int):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        new_comment = Comment(post=post, name = request.POST["name"], content=request.POST["content"])
        new_comment.save()

    
    return redirect("blogApp:post_detail", post.id)