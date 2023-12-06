from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('blog/', blog, name='blog'),
    path('detail/<int:pk>/', detail_view, name='detail'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('u_profile/', u_profile, name='update_profile'),
]
