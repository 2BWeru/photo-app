from django import views
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from . import views




urlpatterns = [
    url('',views.home,name = 'home'),
    url('profile/<id>',views.profile,name = 'users-profile'),
    url('edit_profile/',views.editprofile,name = 'edit_profile'),
    url('post/',views.post,name = 'post'),
    url('show_comments/<id>',views.show_comments,name = 'show_comments'),
    url('like/<int:pk>',views.like_post,name = 'like'),
    url('comments/',views.comments,name = 'comments'),
    url('logout/', LogoutView.as_view(),  name='logout'),
    url('items/',views.search,name = 'search'),
    url('image/<id>',views.details,name = 'details'),
    url('type/<int:id>',views.show,name = 'show-profiles'),
       
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
