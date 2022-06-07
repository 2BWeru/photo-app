from django import views
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from . import views




urlpatterns = [
    path('',views.home,name = 'home'),
    path('profile/<id>',views.profile,name = 'users-profile'),
    path('edit_profile/',views.editprofile,name = 'edit_profile'),
    path('post/',views.post,name = 'post'),
    path('show_comments/<id>',views.show_comments,name = 'show_comments'),
    path('like/<int:pk>',views.like_post,name = 'like'),
    path('comments/',views.comments,name = 'comments'),
    path('logout/', LogoutView.as_view(),  name='logout'),
    path('items/',views.search,name = 'search'),
    path('image/<id>',views.details,name = 'details'),
    path('type/<int:id>',views.show,name = 'show-profiles'),
       
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
