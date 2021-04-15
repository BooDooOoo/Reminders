from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('delete/<int:id_reminder>', delete_reminder, name='delete_reminder'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]