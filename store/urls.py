from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:pk>', views.item, name='item'),
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('category/<str:cat>', views.category, name='category'),
    path('cart', views.cart_summary, name='cart_summary'),
    path('add/', views.cart_add, name='cart_add'),
    path('delete/', views.cart_delete, name='cart_delete'),
    path('update/', views.cart_update, name='cart_update'),
    
]
