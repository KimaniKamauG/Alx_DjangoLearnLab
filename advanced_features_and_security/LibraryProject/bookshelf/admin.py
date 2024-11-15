from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin 
from .models import CustomUser 
# Register your models here.
@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    # Displays the title, author and publication year fields in the list view.
    list_filter = ('publication_year', 'author')
    # Adds filter options by publication year and author.
    search_fields = ('title', 'author')
    # Enables a search bar option by title and author.
    
    class Meta:
        permissions = [
            ('can_view', 'Can view book details'),
            ('can_create', 'Can create a book'),
            ('can_edit', 'Can edit book'),
            ('can_delete', 'Can delete book'),
        ]

#admin.site.register(BookAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )
    list_display = ('username', 'email', 'is_staff', 'date_of_birth')
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
