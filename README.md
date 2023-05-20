# Django OpenAI Chat Application

## Overview
This is a Django-based application designed to interact with OpenAI's GPT models for generating text and image responses. It provides an interface to send user prompts to the GPT models, receives the generated response, and stores them for future reference. It also offers the ability to edit and delete stored responses.

## Features
- Generate text based on user input using OpenAI's GPT models.
- Generate image prompts using OpenAI's GPT models.
- Display the generated response.
- List all the generated responses.
- Edit and delete the responses.

## Requirements
- Python 3.6+
- Django
- OpenAI Python library
- Requests library

## Getting Started

## Installation
1. Clone this repository:
    ```
    git clone https://github.com/tsmith4014/chatgpt_interface.git
    ```
2. Navigate into the project directory:
    ```
    cd <chatgpt_interface.git>
    ```
3. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```

## Configuration
This project requires an OpenAI API key to function. It should be provided through an environment variable named `OPENAI_KEY`.

If you are running the project locally, you can set the environment variable in your terminal:

For Linux/macOS:

```bash
export OPENAI_KEY=your_openai_key
```

For Windows (in Command Prompt):

```cmd
set OPENAI_KEY=your_openai_key
```

For Windows (in PowerShell):

```cmd
$env:OPENAI_KEY="your_openai_key"
```

You can also use a .env file in the root directory to set the environment variables. 
This file should contain key-value pairs representing the environment variables:
    OPENAI_KEY=your_openai_key

Remember to replace your_openai_key with your actual OpenAI API key.
Important: Do not include the .env file in the version control to keep your API key secure.

### Running the Server
After configuration, you can start the Django development server:
```python 
    python manage.py runserver
```
Now you can access the application in your web browser at `http://127.0.0.1:8000/chatgpt/`

### Usage

The application provides a user interface for interacting with OpenAI's GPT models. The home page presents options to either generate text or image responses.

#### Text Generation

By selecting 'Generate Text', you are directed to a form where you can input your prompt and parameters for the GPT model (temperature, top_p, model, and num_tokens).

After submission, the application sends the request to the OpenAI GPT model, retrieves the generated text, and displays it to you. The response is also stored in the database for future reference.

#### Image Generation

By selecting 'Generate Image', you are directed to a form where you can input your prompt and parameters for image generation.

After submission, the application sends the request to the OpenAI GPT model, retrieves the generated image URLs, and displays them to you. The response is also stored in the database for future reference however currently the images are not stored and the user must save the images from the page directly.  *Note this will be improved upon in the future with images being stored to a directroy of choice by the user.

#### Viewing Stored Responses

You can view all stored responses by selecting 'View Stored Responses'. This will display a list of stored responses. You can also edit and delete the stored responses.

## Contributing

Feel free to contribute to this project by creating a pull request. For major changes, please open an issue first to discuss the changes you want to make.

## License

This project is licensed under the MIT License.


