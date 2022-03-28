from django.urls import path, include
from .views import ChatView

urlpatterns = [
    path('<int:pk>/', ChatView.as_view(), name='chat'),

]
