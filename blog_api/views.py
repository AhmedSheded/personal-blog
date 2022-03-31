from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


class BlogListPosts(APIView):

    def get(self, request):
        posts = Post.objects.all()
        # comments = Comment.objects.all()
        # comments_serializer = CommentSerializer(comments, many=True)
        posts_serializer = PostSerializer(posts, many=True)
        return Response(posts_serializer.data, status=status.HTTP_200_OK)


class ViewPost(APIView):

    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        comments = Comment.objects.filter(post=post_id)
        comment_serializer = CommentSerializer(comments, many=True)
        print(comments)
        post_serializer = PostSerializer(post, many=False)
        return Response({"data": post_serializer.data, 'comments': comment_serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, post_id):
        data = {
            'message': request.data.get('message'),
            'post': post_id
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def aboutme(request):
#     return Response(request, status=status.HTTP_200_OK)

