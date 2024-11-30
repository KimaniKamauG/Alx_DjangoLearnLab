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

## Testing the API

You can test the API using tools like Postman or curl. Make sure to include authentication tokens for endpoints that require authentication. 

### Example Commands

- **List Books**:
  ```bash
  curl -X GET http://localhost:8000/api/books/