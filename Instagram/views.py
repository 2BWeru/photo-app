from email.message import EmailMessage
from pyexpat.errors import messages
from urllib import request
from django.conf import settings
from django.forms import ImageField
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from flask_login import user_logged_in
from urllib3 import HTTPResponse
from .models import Post, Profile,Comments
from .email import send_welcome_email
from django.template.loader import render_to_string


# Create your views here.
# def index(request):

#   texts= Profile.objects.all()

#   return render(request,"index.html",{"texts":texts})


def home(request):
  user = request.user
  updates= Post.objects.all()
  comment = Comments.objects.all()
  
  texts= Profile.objects.all()
  

  context = {
   'updates':updates,
   "comment":comment,
   "user":user,
   "texts":texts
   }
  return render(request, 'home.html', context)


# imagedetails
def show_comments(request,id):

  comment= Comments.objects.filter(id=id)
  
  return render(request,"display_comments.html",{"comment":comment})

def details(request,id):

  updates= Post.objects.filter(id=id)
  
  return render(request,"details.html",{"updates":updates})

@login_required(login_url='/accounts/login/')
def profile(request,id):
 
       
  profiles = Profile.objects.filter(id=id)
  updates= Post.objects.all().order_by('image')
  
  
  return render(request, 'Profile/profile.html',{"updates":updates,"profiles":profiles})


@login_required(login_url='/accounts/login/')
def editprofile(request):
   if request.method == "POST":
        prod = Profile()
        prod.name = request.POST.get('name')
        prod.id = request.POST.get('id')
        prod.username = request.POST.get('username')
        prod.bio = request.POST.get('bio')

        if len(request.FILES) != 0:
            prod.avatar = request.FILES['avatar']

        prod.save()
        # messages.success(request, "Profile Updated Successfully")
        
        return redirect('users-profile')

   return render(request, 'Profile/edit_profile.html')
# post
def post(request):
  if request.method == "POST":
        prod = Post()
        prod.name = request.POST.get('name')
        prod.id = request.POST.get('id')
        prod.caption = request.POST.get('caption')
        
        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        # messages.success(request, "Post Updated Successfully")
        return redirect('home')
  return render(request,'addpost.html')

# Comments
@login_required(login_url='/accounts/login/')
def comments(request):
  if request.method == "POST":
          prod = Comments()
          prod.text = request.POST.get('text')

          prod.save()
          # messages.success(request, "Product Added Successfully")
 
          return redirect('show_comments')
  return render(request, 'addcomment.html')

# likes
@login_required(login_url='/accounts/login/')
def like_post(request,pk):
  post =get_object_or_404(Post, id=request.POST.get('post_id'))
  post.likes.add(request.user)

  return HttpResponseRedirect(reverse('index', args=[str(pk)]))
  
# search
def search(request):
    if "profile" in request.GET and request.GET["profile"]:
        searched_item=request.GET["profile"]
        items= Profile.search_by_name(searched_item)
        message = f"{searched_item}"


        return render(request, 'search/search.html',{"message":message,"items":items})
    else:
        message = "Kindly input a search term to get any results"
        return render(request, 'search/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def logout(request):
    return render(request, 'registration/registration_form.html')

# display
def show(request,id):
    try:
        profiles = Profile.objects.get(id=id)
        
       
        context = {}
        context['profiles'] = profiles

    except:
        ValueError
        raise 'Error'
    return render(request, "search/display_search.html",context)


# email

def email(request,uid):
  template = render_to_string("instagram/email/email.html",{'name':request.user.profile.username})
  email= EmailMessage(
    "Thanks for logging in to Instagram",
    template,
    settings.EMAIL_HOST_USER,
    ["lucy5@gmail.com"],
  )

  email.fail_silently='false'

  email.send()
            #.................
  return render(request,'index.html')

