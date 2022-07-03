from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
]