from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('item', views.item, name='item'),
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
]
