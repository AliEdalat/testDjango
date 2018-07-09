from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/aut', views.authentication, name='authentication'),
    path('login/signup', views.signup, name='signup'),
    path('login/signup_new_user', views.signup_new_user, name='signup_new_user'),
]