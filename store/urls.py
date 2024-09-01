from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('item ', views.item, name='item'),
    path('login ', views.login_user, name='login'),
    path('logout ', views.login_user, name='logout'),
]
