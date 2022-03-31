from django.urls import path
from .views import *
urlpatterns = [
    path('', BlogListPosts.as_view()),
    path('post/<int:post_id>/', ViewPost.as_view()),
    # path('about_me/',aboutme)
]