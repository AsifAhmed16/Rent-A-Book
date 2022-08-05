from django.urls import path, include
from .views import *

app_name = 'management'

urlpatterns = [
    path('', home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('book_details/<int:id>', book_details, name='book_details'),
    path('rent_book/<int:id>', rent_book, name='rent_book'),
    path('rent_list/', rent_list, name='rent_list'),
]
