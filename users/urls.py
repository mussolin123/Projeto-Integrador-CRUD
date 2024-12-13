from django.urls import path
from .views import UserRegisterAPIView

urlpatterns = [
    
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('', UserRegisterAPIView.as_view(), name='user-list') 
]