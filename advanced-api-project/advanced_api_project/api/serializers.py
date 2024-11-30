from rest_framework import serializers 
from .models import Author, Book 
from datetime import date 

# BookSerializer ensures all fields of the Book model are serialized.
# Includes custom validation to prevent invalid publication year.
# AuthorSerializer dynamically serializes an author's books using nested serialization. 

class BookSerializer(serializers.ModelSerializer):
    ''' 
    Serializer for the book model.
    Includes a validation method to ensure the publication year in not in the future.
    '''
    class Meta:
        model =Book 
        fields = ['__all__']

        def validate_publication_year(self, value):
            current_year = date.today().year
            if value > current_year:
                raise serializers.ValidationError('Publication year cannot be in the future.')
            return value 
        
class AuthorSerializer(serializers.ModelSerializer):
    '''
    Serializer for teh author model.
    Includes nested serialization for related books.
    '''
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
