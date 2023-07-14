from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('top-up/', views.top_up_balance, name='top_up_balance'),
    path('withdraw/', views.withdraw_balance, name='withdraw_balance'),
    path('movies/<str:movie_title>/', views.movie_detail, name='movie_detail'),
    path('movies/<str:movie_title>/book-ticket/', views.book_ticket, name='book_ticket'),
    path('transactions/<int:transaction_id>/cancel/', views.cancel_ticket, name='cancel_ticket'),
    path('transactions/', views.transaction_history, name='transaction_history'),
]
