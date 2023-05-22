# tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import GPTSub, ImagePrompt
from .forms import GPTRequestForm, ImagePromptForm, EditGPTSubResponseForm
from unittest.mock import patch

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_gpt_sub = GPTSub.objects.create(
            prompt='Test Prompt',
            temperature=1.0,
            top_p=0.9,
            model='gpt-3.5-turbo',
            response_name='Test Response',
            response = 'Test Response',
            tokens_used=100,
            prompt_tokens=50,
            response_tokens=50
        )

        self.test_image_prompt = ImagePrompt.objects.create(
            prompt='Test Prompt',
            n=1,
            size='1024x1024',
            response_format='url'
        )

        self.index_url = reverse('home')
        self.gpt_sub_url = reverse('gpt_request')
        self.gpt_response_url = reverse('gpt_response', args=[self.test_gpt_sub.id])
        self.gpt_sub_responses_url = reverse('gpt_sub_response_list')
        self.edit_gpt_sub_response_url = reverse('gpt_sub_response_edit', args=[self.test_gpt_sub.id])
        self.delete_gpt_sub_response_url = reverse('gpt_sub_response_delete', args=[self.test_gpt_sub.id])
        self.image_prompt_request_url = reverse('image_prompt_request')
        self.image_prompt_response_url = reverse('image_prompt_response', args=[self.test_image_prompt.id])

    @patch('openai.Completion.create')
    def test_handle_gpt_response_GET(self, mock_create):
        mock_create.return_value = {"choices": [{"text": "Test Response"}]}
        response = self.client.get(self.gpt_response_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gpt_response.html')

    @patch('openai.Completion.create')
    def test_handle_gpt_request_POST(self, mock_create):
        mock_create.return_value = {"choices": [{"text": "Test Response"}]}
        response = self.client.post(self.gpt_sub_url, {
            'prompt': 'Test Prompt',
            'temperature': 1.0,
            'top_p': 0.9,
            'model': 'gpt-3.5-turbo',
            'response_name': 'Test Response',
            'response': 'Test Response',
            'tokens_used': 100,
            'prompt_tokens': 50,
            'response_tokens': 50
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(GPTSub.objects.count(), 2)

    @patch('requests.post')
    def test_handle_image_prompt_request_POST(self, mock_post):
        mock_post.return_value.json.return_value = {'data': [{'url': 'http://test.url'}]}
        response = self.client.post(self.image_prompt_request_url, {
            'prompt': 'Test Prompt',
            'n': 1,
            'size': '1024x1024',
            'response_format': 'url'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(ImagePrompt.objects.count(), 2)


# Add these to your TestViews class:

    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_list_gpt_sub_responses_GET(self):
        response = self.client.get(self.gpt_sub_responses_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gpt_sub_response_list.html')

    def test_edit_gpt_sub_response_GET(self):
        response = self.client.get(self.edit_gpt_sub_response_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gpt_sub_response_edit.html')

    def test_delete_gpt_sub_response_GET(self):
        response = self.client.get(self.delete_gpt_sub_response_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gpt_sub_response_confirm_delete.html')

    @patch('requests.post')
    def test_handle_image_prompt_response_GET(self, mock_post):
        mock_post.return_value.json.return_value = {'data': [{'url': 'http://test.url'}]}
        response = self.client.get(self.image_prompt_response_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'image_prompt_response.html')
