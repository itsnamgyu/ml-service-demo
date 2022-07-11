from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),

    path('app', views.AppView.as_view(), name='app'),
    path('api/posts/', views.PostListApiView.as_view(), name='post_list_api'),
    path('api/posts/create/', views.PostCreateApiView.as_view(), name='post_create_api'),
]
