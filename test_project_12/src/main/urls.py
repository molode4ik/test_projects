from django.urls import path
from src.main.views import index, register, user_login, user_logout

urlpatterns = [
    path('index/', index, name='index'),
    path('register/', register, name='register'),
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
