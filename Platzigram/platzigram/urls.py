from django.contrib import admin
from django.urls import path

from platzigram import views as local_views
from posts import views as posts_views




urlpatterns = [
    
    path('hello-world/', local_views.hello_world),

    path('posts/', posts_views.list_posts)

]
