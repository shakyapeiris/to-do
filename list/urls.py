from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.loginPage, name = "login"),
    path('', views.home, name = "home"),
    path('logout/', views.logoutPage, name = "logout"),
    path('delete/<int:my_task>', views.delete, name = 'delete'),
    path('update/<int:up_task>', views.update, name = 'update')
]