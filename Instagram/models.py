
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    name = models.CharField(null=True,max_length=50)
    id = models.CharField(max_length=50,primary_key=True, unique=True, blank=True)
    user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE, blank=True, null=True)
    username=models.CharField(null=True,max_length=50)
    bio=models.TextField(null=True,max_length=200)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images',null=True, blank=True)
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self): 
        self.delete()
  

    @classmethod
    def search_by_name(cls,searched_term):
        profile = cls.objects.filter(name__icontains=searched_term)
        return profile


    def __str__(self):
        return (self.username)

class Post(models.Model):
    name = models.CharField(null=True,max_length=50)
    caption = models.TextField(null=True,max_length=50)
    id=models.CharField(max_length=50,primary_key=True, unique=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='photo_images')
    likes = models.ManyToManyField(User,default=None, blank=True)
    comment = models.ManyToManyField(User,default=None, blank=True,related_name='comments')
    created=models.DateTimeField(auto_now=True)

    def save_post(self):
        self.save()
    
    def delete_post(self): 
        self.delete()

    @classmethod
    def update_image(cls,current_img,new_img):
        updated_img = Post.objects.filter(image_name=current_img).update(name=new_img)
        return updated_img


    def __str__(self):
        return (self.name)

   
# create tuple


class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.post


class Comments(models.Model):
    user = models.OneToOneField(User, related_name='user',on_delete=models.CASCADE, blank=True, null=True)
    post=models.ManyToManyField(Post)
    posted=models.DateTimeField(auto_now=True)
    text=models.TextField(null=True,max_length=50)

    def __str__(self):
        return self.text