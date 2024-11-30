This is a Project that involves the use of Django Rest Framework to perform the following functions.

### Books API Endpoints

- **List Books**
  - **Endpoint**: `GET /api/books/`
  - **Description**: Retrieves a list of all books.
  - **Permissions**: Open to all users (authenticated and unauthenticated).

- **Retrieve a Book**
  - **Endpoint**: `GET /api/books/<int:pk>/`
  - **Description**: Retrieves details of a specific book by its ID.
  - **Permissions**: Open to all users (authenticated and unauthenticated).

- **Create a Book**
  - **Endpoint**: `POST /api/books/create/`
  - **Description**: Creates a new book entry.
  - **Request Body**:
    ```json
    {
        "title": "New Book",
        "author": "Author Name",
        "published_date": "2023-01-01",
        "isbn": "1234567890123"
    }
    ```
  - **Permissions**: Restricted to authenticated users only.

- **Update a Book**
  - **Endpoint**: `PUT /api/books/update/<int:pk>/`
  - **Description**: Updates an existing book entry.
  - **Request Body**:
    ```json
    {
        "title": "Updated Book",
        "author": "Updated Author",
        "published_date": "2023-02-01",
        "isbn": "1234567890123"
    }
    ```
  - **Permissions**: Restricted to authenticated users only.

- **Delete a Book**
  - **Endpoint**: `DELETE /api/books/delete/<int:pk>/`
  - **Description**: Deletes a specific book entry by its ID.
  - **Permissions**: Restricted to authenticated users only.

## Customizations

- **BookCreateView**: The `perform_create` method can be overridden to add custom logic before saving a new book. Currently, it simply saves the book.
  
- **Permissions**: The API uses DRF's built-in permission classes to restrict access to create, update, and delete operations to authenticated users.

# Advanced API Project

## Overview

This project provides a RESTful API for managing books using Django REST Framework. The API supports CRUD operations and includes advanced query capabilities such as filtering, searching, and ordering.

## API Endpoints

### Books

- **List Books**
  - **Endpoint**: `GET /api/books/`
  - **Description**: Retrieves a list of all books with filtering, searching, and ordering capabilities.
  - **Permissions**: Open to all users (authenticated and unauthenticated).

### Filtering

You can filter the list of books by the following fields:

- **title**: Filter books by title (case-insensitive).
- **author**: Filter books by author (case-insensitive).
- **published_year**: Filter books by the year of publication.

#### Example Requests

- **Filter by Title**:
  ```bash
  curl -X GET "http://localhost:8000/api/books/?title=Uoga"

## Testing the API

You can test the API using tools like Postman or curl. Make sure to include authentication tokens for endpoints that require authentication. 

### Example Commands

- **List Books**:
  ```bash
  curl -X GET http://localhost:8000/api/books/



# Advanced API Project - Unit Testing

## Overview

This project provides a RESTful API for managing books using Django REST Framework. This document outlines the unit tests created to ensure the integrity of the API endpoints, focusing on CRUD operations, filtering, searching, ordering functionalities, and permission controls.

## Testing Framework

The unit tests are built using Django's built-in testing framework, which is based on Python's `unittest` module. The tests are located in the `api/test_views.py` file.

## Test Cases

### 1. Setup

The `setUp` method creates a test user and a sample book instance for testing. The user is logged in to simulate authenticated requests.

### 2. Test Scenarios

#### a. Create Book

- **Test Method**: `test_create_book`
- **Description**: Tests the creation of a new book.
- **Expected Outcome**: Should return a `201 Created` status and the book should be saved in the database.

#### b. Retrieve Book

- **Test Method**: `test_retrieve_book`
- **Description**: Tests retrieving a book by its ID.
- **Expected Outcome**: Should return a `200 OK` status and the correct book data.

#### c. Update Book

- **Test Method**: `test_update_book`
- **Description**: Tests updating an existing book.
- **Expected Outcome**: Should return a `200 OK` status and the book's data should be updated in the database.

#### d. Delete Book

- **Test Method**: `test_delete_book`
- **Description**: Tests deleting a book by its ID.
- **Expected Outcome**: Should return a `204 No Content` status and the book should be removed from the database.

#### e. Filter Books

- **Test Method**: `test_filter_books`
- **Description**: Tests filtering books by title.
- **Expected Outcome**: Should return a `200 OK` status and the correct number of books matching the filter.

#### f. Search Books

- **Test Method**: `test_search_books`
- **Description**: Tests searching books by author.
- **Expected Outcome**: Should return a `200 OK` status and the correct number of books matching the search term.

#### g. Order Books

- **Test Method**: `test_order_books`
- **Description**: Tests ordering books by title.
- **Expected Outcome**: Should return a `200 OK` status and the books should be ordered correctly.

#### h. Permission Denied on Create Without Auth

- **Test Method**: `test_permission_denied_on_create_without_auth`
- **Description**: Tests that unauthenticated users cannot create a book.
- **Expected Outcome**: Should return a `403 Forbidden` status.

## Running the Tests

To run the test suite, use the following command:

```bash
python manage.py test api