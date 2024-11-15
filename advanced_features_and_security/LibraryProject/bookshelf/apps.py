from django.apps import AppConfig
# from django.db.models.signals import post_save 
# from django.contrib.auth import get_user_model 
# from .models import CustomUser 

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'
    # verbose_name = 'Bookshelf'

    # def ready(self):
    #     post_save.connect(create_custom_user, sender=get_user_model())
    