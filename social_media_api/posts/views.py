from django.shortcuts import render
#from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer, LikeSerializer 
from .models import Post, Comment, Like 
#from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView,  UpdateAPIView, DestroyAPIView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework import filters

from rest_framework import generics, permissions, mixins
from django.core.exceptions import PermissionDenied

from notifications.models import Notification
from django.shortcuts import get_object_or_404 
from django.db.models.signals import post_save 
from django.dispatch  import receiver 

# Create your views here.
class PostPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter]
    def get(self, request):
        posts = Post.objects.all()
        paginated_post = PostPagination().paginate_queryset(queryset=posts, request=request)
        serializer = PostSerializer(paginated_post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

    # def get(self):
    #     queryset = Post.objects.all()
    #     title = self.request.query_params.get('title')
    #     if title is not None:
    #         queryset = queryset.filter(title__icontains=title)
    #     return queryset
    
# Create View of the Posts API
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostUpdateView(generics.UpdateAPIView, LoginRequiredMixin, UserPassesTestMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    

class PostDetailView(generics.ListAPIView):
    def get(self, request):
        post = Post.objects.all().get(id=request.data['id'])
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)



class PostDeleteView(generics.DestroyAPIView, LoginRequiredMixin, UserPassesTestMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, pk):
        post = self.get_object(pk)
        if post.author == request.user:
            post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class PostSearchView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, request):
        search_term = request.GET.get('search_term')
        title_q = Q(title__icontains=search_term) if search_term else Q()
        content_q = Q(content__icontains=search_term) if search_term else Q()
        results = Post.objects.filter(title_q).filter(content_q)
        return results 


class CommentPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class CommentListView(generics.ListAPIView):
    pagination_class = CommentPagination
    filter_backends = [filters.SearchFilter]

    def get(self, request, **kwargs):
        pk = self.kwargs['pk']
        post = Post.objects.get(id=pk)
        comments = Comment.objects.filter(post=post)
        paginated_comments = CommentPagination().paginate_queryset(queryset=comments, request=request)
        serializer = CommentSerializer(paginated_comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CommentCreateView(generics.CreateAPIView, LoginRequiredMixin, UserPassesTestMixin):
    serializer_class = CommentSerializer

    def post(self, request):
        serializer  = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentUpdateView(generics.UpdateAPIView, LoginRequiredMixin, UserPassesTestMixin):
    def post(self, request):
        serializer  = CommentSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            comment = Comment.objects.get(id=request.data['pk'])
            if self.user != request.user:
                raise PermissionDenied('Author is the only one allowed to edit.')
            if comment.author == request.user:
                serializer.update(Comment, serializer.validated_data)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CommentDetailView(generics.ListAPIView, LoginRequiredMixin, UserPassesTestMixin):
    def get(self, request):
        comment = Comment.objects.all().get(id=request.data['id'])
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CommentDeleteView(generics.DestroyAPIView, LoginRequiredMixin, UserPassesTestMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, pk):
        comment = self.get_object(pk)
        if comment.author == request.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class FeedView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.users.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikePostView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs['pk']
        post = generics.get_object_or_404(Post, pk=post_id)
        Like.objects.get_or_create(user=self.request.user, post=post)
        if Like.objects.filter(user=self.request.user, post=post).exists():
            # Showing post is already liked by the user 
            return Response({'error': 'Seems you have liked this post already'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data={'post': post, 'user': self.request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@receiver(post_save, sender=Like)
def send_notification(sender, instance, **kwargs):
    liker = instance.user
    post = instance.post

    # Create a notification for the post owner
    Notification.objects.create(
        user=liker, # This is the recipient.
        message=f'{liker.username} liked your post: {post.title}',  # Notification message 
        link=post.get_absolute_url()  # Link to the post 
    )

class UnlikePostView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        like = get_object_or_404(Like, post__pk=pk, user=self.request.user)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#'generics.get_object_or_404(Post, pk=pk'
#'Like.objects.get_or_create(user=request.user, post=post)'
    










# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = ['IsAuthenticatedOrReadOnly']

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

