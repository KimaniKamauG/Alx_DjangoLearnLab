from rest_framework import serializers 
from .models import Post, Comment, Like 
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like 
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data['user']
        post = validated_data['post']

        existing_instance = Like.objects.filter(user=user, post=post).first()
        
        if existing_instance:
            return existing_instance

        return super().create(validated_data)