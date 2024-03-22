from django.contrib import admin
from django.urls import path, include
from . import views
# import settings

urlpatterns = [
     path('postComment', views.postComment, name="postComment"),
    path('', views.blogHome, name="bloghome"),
    path('<str:slug>', views.blogPost, name="blogPost"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)