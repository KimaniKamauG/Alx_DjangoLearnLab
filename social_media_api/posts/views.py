from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer 
from .models import Post, Comment 
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView,  UpdateAPIView, DestroyAPIView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework import filters 

# Create your views here.
class PostPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    permission_classes = ['IsAuthenticatedOrReadOnly']
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
class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = ['IsAuthenticatedOrReadOnly']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostUpdateView(UpdateAPIView, LoginRequiredMixin, UserPassesTestMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = ['IsAuthenticatedOrReadOnly']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    

class PostDetailView(ListAPIView):
    def get(self, request):
        post = Post.objects.all().get(id=request.data['id'])
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)



class PostDeleteView(DestroyAPIView, LoginRequiredMixin, UserPassesTestMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = ['IsAuthenticatedOrReadOnly']

    def delete(self, request, pk):
        post = self.get_object(pk)
        if post.author == request.user:
            post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class PostSearchView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = ['IsAuthenticatedOrReadOnly']

    def get_queryset(self, request):
        search_term = request.GET.get('search_term')
        title_q = Q(title__icontains=search_term) if search_term else Q()
        content_q = Q(content__icontains=search_term) if search_term else Q()
        results = Post.objects.filter(title_q).filter(content_q)
        return results 








class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = ['IsAuthenticatedOrReadOnly']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

