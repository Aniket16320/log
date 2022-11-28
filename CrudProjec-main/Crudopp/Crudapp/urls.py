from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('register/', views.register, name='register' ),
    path('login_user/', views.login_user, name='login_user' ),
    path('logout_user', views.logout_user, name='logout' ),
    path('add/', views.add_show, name='add' ),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('<int:id>/', views.update_data, name='updatedata'),

   

]