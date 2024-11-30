from rest_framework.test import APITestCase 
from rest_framework import status 
from .models import Book, Author 
from django.contrib.auth.models import User 

class BookAPITestCase(APITestCase):
    '''
    Test suite for the Book API endpoints.
    '''
    def setUp(self):
        # Create a User for authentication purposes 
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create an Author and Books for testing purposes 
        self.author = Author.objects.create(name='Kai Cenat')
        self.book1 = Book.objects.create(title='Mafiathon', publication_year=2021, author=self.author)
        self.book2 = Book.objects.create(title='Mafiathon 2', publication_year=2023, author=self.author)

        # EndPoints for testing
        self.book_list_url = 'api/books/'
        self.book_detail_url = f'api/books/{self.book1.id}/'

    def test_list_books(self):
        '''
        Test retrieving the list of books.
        ''' 
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) # Ensure two books are returned 
        print(response.content)

    def test_create_book(self):
        '''
        Test creating a new book.
        '''
        self.client.login(username='testuser', password='testpassword') # login
        payload = {
            'title': 'Mafiathon 3', 
            'publication_year': 2024,
            'author': self.author.id,
        }
        response = self.client.post(self.book_list_url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'Mafiathon 3')

    def test_update_book(self):
        '''
        Test updating an existing book.
        '''
        self.client.login(username='testuser', password='testpassword')
        payload = {'title': 'Mafiathon 3 Miles Morales'}
        response = self.client.patch(self.book_detail_url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Mafiathon 3 Miles Morales')
        print(response.content)

    def test_delete_book(self):
        '''
        Test deleting an existing book.
        '''
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
        print(response.content)

    def test_filter_books_by_author(self):
        '''
        Test filtering books by author.
        '''
        response = self.client.get(self.book_list_url, {'search': 'Miles'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        print(response.content)

    def test_search_books(self):
        '''
        Test searching for books by title and author name.
        '''
        response = self.client.get(self.book_list_url, {'search': 'Mafiathon'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Mafiathon 3 Miles Morales')
        print(response.content)

    def test_order_books_by_publication_year(self):
        '''
        Test ordering books by publication year.
        '''
        response = self.client.get(self.book_list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2021)
        self.assertEqual(response.data[1]['publication_year'], 2023)
        print(response.content)

