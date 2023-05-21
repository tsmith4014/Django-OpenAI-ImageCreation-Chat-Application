#urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('chatgpt/', views.handle_gpt_request, name='gpt_request'),
    path('chatgpt/response/<int:pk>', views.handle_gpt_response, name='gpt_response'),
    path('image_prompt/', views.handle_image_prompt_request, name='image_prompt_request'),
    path('image_prompt/response/<int:pk>', views.handle_image_prompt_response, name='image_prompt_response'),
    path('gpt_sub_responses/', views.list_gpt_sub_responses, name='gpt_sub_response_list'),
    path('gpt_sub_responses/<int:pk>/edit/', views.edit_gpt_sub_response, name='gpt_sub_response_edit'),
    path('gpt_sub_responses/<int:pk>/delete/', views.delete_gpt_sub_response, name='gpt_sub_response_delete'),
]
