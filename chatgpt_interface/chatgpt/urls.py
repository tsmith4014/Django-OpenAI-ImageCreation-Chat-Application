#urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='gpt_index'),
    path('chatgpt/', views.handle_gpt_request, name='gpt_request'),
    path('chatgpt/response/<int:pk>', views.handle_gpt_response, name='gpt_response'),
]
