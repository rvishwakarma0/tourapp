from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('log',views.profile),
    path('register/', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout')

]