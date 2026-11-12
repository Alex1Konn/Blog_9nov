from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('profile/', views.user_profile, name='profile')
]

