from pyexpat.errors import messages
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from urllib3 import HTTPResponse
from .models import Like, Post, Profile,Comments,User



# Create your views here.

def index(request):

  updates= Post.objects.all()
  comment = Comments.objects.all()


  context = {
   'comment':comment,
   'updates':updates,
   }

  return render(request ,'index.html',context)

@login_required(login_url='/accounts/login/')
def profile(request):

  texts= Profile.objects.all()
  context = {'texts':texts}

  return render(request, 'Profile/profile.html',context)


@login_required(login_url='/accounts/login/')
def editprofile(request):
   if request.method == "POST":
        prod = Profile()
        prod.name = request.POST.get('name')
        prod.username = request.POST.get('username')
        prod.bio = request.POST.get('bio')

        if len(request.FILES) != 0:
            prod.avatar = request.FILES['avatar']

        prod.save()
        messages.success(request, "Profile Updated Successfully")
        return redirect('users-profile')

   return render(request, 'Profile/edit_profile.html')
# post
def post(request):
  if request.method == "POST":
        prod = Post()
        prod.name = request.POST.get('name')
        prod.caption = request.POST.get('caption')
        
        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        # messages.success(request, "Post Updated Successfully")
        return redirect('index')
  return render(request,'addpost.html')

# Comments
@login_required(login_url='/accounts/login/')
def comments(request):
  if request.method == "POST":
          prod = Comments()
          prod.text = request.POST.get('text')

          prod.save()
          messages.success(request, "Product Added Successfully")
          return redirect('index')
  return render(request, 'index.html')

# likes
@login_required(login_url='/accounts/login/')
def like_post(request):
  user= request.user
  post = Post.objects.get()

  current_likes = post.likes
  liked = Like.object.filter(user=user,post=post).count

  if not liked:
    liked = Like.objects.create(user=user, post=post)
    current_likes = current_likes + 1
  else:
    liked = Like.object.filter(user=user,post=post).delete()
    current_likes = current_likes - 1

  post.likes = current_likes
   
  post.save()

  return HttpResponseRedirect(reverse('post' , args=[]))
  
# search
def search(request):
    if "profile" in request.GET and request.GET["profile"]:
        searched_item=request.GET["profile"]
        items= Profile.search_by_name(searched_item)
        message = f"{searched_item}"


        return render(request, 'search/search.html',{"message":message,"items":items})
    else:
        message = "Kindly input a search term to get any results"
        return render(request, 'main/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def logout(request):
    return render(request, 'registration/registration_form.html')

# display
def show(request,id):
    try:
        profiles = Profile.objects.get(id=id)
        
       
        context = {}
        context['profile'] = profiles

    except:
        ValueError
        raise 'Error'
    return render(request, "main/show-category.html",context)





 
