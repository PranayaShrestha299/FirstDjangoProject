
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('room/<str:pk>/',views.room, name='room'),
    path('create-room/', views.createroom, name='create-room'),
    path('update-room/<str:pk>/', views.updateroom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteroom, name='delete-room'),
    path('register/', views.loginRegister, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]
