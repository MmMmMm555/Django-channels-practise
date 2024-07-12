from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:room_id>', views.chat_view, name='chat'),
    # Add other URL patterns as needed
]
