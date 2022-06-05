from django import views
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from . import views




urlpatterns = [
    path('',views.index,name = 'index'),
    path('profile/',views.profile,name = 'users-profile'),
    path('edit_profile/',views.editprofile,name = 'edit_profile'),
    path('post/',views.post,name = 'post'),
    path('like/',views.like_post,name = 'like'),
    path('comments/',views.comments,name = 'comments'),
    path('logout/', LogoutView.as_view(),  name='logout'),
    path('items/',views.search,name = 'search'),
    path('type/<int:id>',views.show,name = 'show-profiles'),
       
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
