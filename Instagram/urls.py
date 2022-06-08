from django import views
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from . import views




urlpatterns = [
    url('^$',views.home,name = 'home'),
    url(r'^profile/(\d+)',views.profile,name = 'users-profile'),
    url(r'^edit_profile/',views.editprofile,name = 'edit_profile'),
    url(r'^post/',views.post,name = 'post'),
    url(r'^show_comments/<id>',views.show_comments,name = 'show_comments'),
    url(r'^like/<int:pk>',views.like_post,name = 'like'),
    url(r'^comments/',views.comments,name = 'comments'),
    url(r'^logout/$', LogoutView.as_view(),  name='logout'),
    url(r'^items/',views.search,name = 'search'),
    url(r'^image/<int:id>',views.details,name = 'details'),
    url(r'^type/<int:id>',views.show,name = 'show-profiles'),
    
       
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
