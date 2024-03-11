from django.urls import path, include
from . import views
from .forms import *

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.UserSignupView.as_view(), name="register"),
    path('login/', views.UserLoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('logout/', views.logout_user, name="logout"),
    path('create/', views.create_pizza, name='create'),
    path('create/order', views.order_pizza, name='order'),
    path('completed', views.view_completed, name='completed'),
    path('about', views.about, name='about'),
]