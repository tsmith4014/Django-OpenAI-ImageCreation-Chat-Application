# Django OpenAI Chat Application - VSCode installation instructions  


![Python Version](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Django Version](https://img.shields.io/badge/Django-3.2+-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT3-orange.svg)
![License](https://img.shields.io/badge/License-MIT-red.svg)


![Sunny Day On Mars](/chatgpt_interface/chatgpt/static/mars.png)

## Overview

This is a Django-based application designed to interact with OpenAI's GPT models for generating text and image responses. It provides an interface to send user prompts to the GPT models, receives the generated response, and stores them for future reference. It also offers the ability to edit and delete stored responses.

![Mars War](/chatgpt_interface/chatgpt/static/marswar.png)

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

## Command Line Navigation Instructions

This "nested" README provides a brief guide on how to navigate directories using the command line interface for both Unix (MacOS/Linux) and PowerShell (Windows).

## Unix (MacOS/Linux)

1. **List the contents of the current directory:**
    ```bash
    ls
    ```

2. **Change to a different directory:**
    ```bash
    cd [directory name]
    ```
    Replace `[directory name]` with the name of the directory you want to navigate to.

3. **Move back one directory:**
    ```bash
    cd ..
    ```

4. **Go to the home directory:**
    ```bash
    cd ~
    ```

5. **Create a new directory:**
    ```bash
    mkdir [new-directory]
    ```
    Replace `[new-directory]` with the name of the new directory you want to create.

6. **Delete a directory:**
    ```bash
    rmdir [directory-name]
    ```
    Replace `[directory-name]` with the name of the directory you want to remove.

## PowerShell (Windows)

1. **List the contents of the current directory:**
    ```powershell
    Get-ChildItem
    ```

2. **Change to a different directory:**
    ```powershell
    Set-Location [directory name]
    ```
    Replace `[directory name]` with the name of the directory you want to navigate to.

3. **Move back one directory:**
    ```powershell
    Set-Location ..
    ```

4. **Go to the home directory:**
    ```powershell
    Set-Location ~
    ```

5. **Create a new directory:**
    ```powershell
    New-Item -ItemType directory -Path .\[new-directory]
    ```
    Replace `[new-directory]` with the name of the new directory you want to create.

6. **Delete a directory:**
    ```powershell
    Remove-Item [directory-name]
    ```
    Replace `[directory-name]` with the name of the directory you want to remove.


# Getting Started

## Installation

1. Create a new folder/directory on your machine and clone this repository :

    ```markdownlint
    git clone https://github.com/tsmith4014/Django-OpenAI-ImageCreation-Chat-Application.git
    ```

2. Navigate into the project directory "Django-OpenAI-ImageCreation-Chat-Application" this takes some knowledge of command line prompts but a key has been included with the required, and then some, commands.  You know you are in the correct directory when you do ls (mac/unix) or Get-ChildItem (Windows) and you see chatgpt_interface, .gitignore, README.md, and the requirements.txt we will use to install our dependincies.  
   - On Unix or MacOS:

    ```markdownlint
    cd Django-OpenAI-ImageCreation-Chat-Application
    ```
    
   - On Windows:
   
    ```markdownlint
     Set-Location -Path "Django-OpenAI-ImageCreation-Chat-Application"
    ```

3. Next step we create a virtual environment:

    ```markdownlint
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:

      ```markdownlint
      venv\Scripts\activate
      ```

    - On Unix or MacOS:

      ```markdownlint
      source venv/bin/activate
      ```

5. Install the required Python packages:

    ```markdownlint
    pip install -r requirements.txt
    ```

## Configuration

This project requires an OpenAI API key to function, please go here https://platform.openai.com/docs/api-reference/introduction if you do not have a key and note this is a paid API key but its pretty cheap to run pricing here https://openai.com/pricing. It should be provided through an environment variable named `OPENAI_KEY`.

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

***Django Secret Key!
In the settings.py file that in located at this level Django-OpenAI-ImageCreation-Chat-Application\chatgpt_interface\chatgpt_interface\settings.py must be addressed : SECRET_KEY = config('DJANGO_SECRET_KEY') 
It is recommed this be set in your .env and the DJANGO_SECRET_KEY can literally be a made up string of your choosing.  Another less secure workout is to just change this in settings.py from SECRET_KEY = config('DJANGO_SECRET_KEY') to SECRET_KEY = "kasljdflk8927345oasdjkfh9823745t"  (just some random key) but this is not recommend.

Using a .env (enviroment file) to store keys is easy, at the Django-OpenAI-ImageCreation-Chat-Application project level and at the same level as the .gitignore, requirements.txt create a new file and call it .env, you can tell a .env file because it looks like a little machine cog.  Inside the .env create 2 variables like this: 

      ```markdownlint
      DJANGO_SECRET_KEY = "asdfasdfsds233532454" 
      OPENAI_KEY = "asdfasdf"
      ```

Remember to replace your_openai_key and DJANGO_SECRET_KEY with your keys and remember the DJANGO_SECRET_KEY can be anything you want but the OpenAI access key must be a valid key and please note this will cost money for each request that is made.

Important: Do not include the .env file in the version control to keep your API key secure, it has been added to the .gitignore for your safety, do not remove it.

## Migrations and Running the Server

Django uses a migration system for tracking changes to your models and applying them to your database schema. Migrations are stored as an on-disk format, referred to here as "migration files". These files are actually just normal Python files with an agreed-upon object layout, written in a declarative style.

Start the Django development server by navigating to the root directory of the project "chatgpt_interface" and running the following commands:

1. Make Migrations 
```markdownlint
python manage.py makemigrations
```

2. Make Migrations 
```markdownlint
python manage.py migrate
```

3. Start the Server
```markdownlint
python manage.py runserver
```

Now you can access the application in your web browser at `http://127.0.0.1:8000/chatgpt/`

## Usage

The application provides a user-friendly form to submit your prompts to the GPT models. You can specify various parameters like temperature, top_p, model, and num_tokens.

Once you submit the form, the application sends a request to the OpenAI API and shows the generated response. The responses are stored in a database and can be viewed, edited, and deleted later.

For generating image prompts, the application provides a different form where you can specify the prompt, n, size, and response_format. The generated images are displayed in the response.

## Text Generation

By selecting 'Generate Text', you are directed to a form where you can input your prompt and parameters for the GPT model (temperature, top_p, model, and num_tokens).

After submission, the application sends the request to the OpenAI GPT model, retrieves the generated text, and displays it to you. The response is also stored in the database for future reference.

## Image Generation

By selecting 'Generate Image', you are directed to a form where you can input your prompt and parameters for image generation.

After submission, the application sends the request to the OpenAI GPT model, retrieves the generated image URLs, and displays them to you. The response is also stored in the database for future reference however currently the images are not stored and the user must save the images from the page directly.  *Note this will be improved upon in the future with images being stored to a directroy of choice by the user.

## Viewing Stored Responses

You can view all stored responses by selecting 'View Stored Responses'. This will display a list of stored responses. You can also edit and delete the stored responses.

## Troubleshooting

Should you encounter any issues during the setup or operation of the application, here are some common problems and their solutions:

1. **Missing OPENAI_KEY environment variable:** If you haven't set your OPENAI_KEY environment variable, you will encounter an error when trying to interact with the GPT models. Ensure that you have an OpenAI API key and that it is correctly set as an environment variable.

2. **Package not found during installation:** This could be due to an outdated pip version. Ensure that your pip package installer is up-to-date by running `pip install --upgrade pip`.

3. **Issues running the Django server:** Make sure that you are running the server command (`python manage.py runserver`) in the root directory of the project where the `manage.py` file is located.

4. **Images not being displayed in the Image Generation section:** Currently, the application does not store the generated images, but only the URLs of the images. Hence, you need to save the images directly from the page.

## Running the Unit-Tests

You can run the application tests using Django's test runner. In the project root directory, run the following command:

```markdownlint
python manage.py test chatgpt
```


# Additional Command Line Instructions

This README extends the previous guide with more command line instructions for Unix (MacOS/Linux) and PowerShell (Windows).

## Unix (MacOS/Linux)

1. **Print the current directory:**
    ```bash
    pwd
    ```

2. **Create a new file:**
    ```bash
    touch [file-name]
    ```
    Replace `[file-name]` with the name of the file you want to create.

3. **Open a file using the default editor:**
    ```bash
    open [file-name]
    ```
    Replace `[file-name]` with the name of the file you want to open.

4. **Show the top of a file's contents:**
    ```bash
    head [file-name]
    ```
    Replace `[file-name]` with the name of the file.

5. **Show the bottom of a file's contents:**
    ```bash
    tail [file-name]
    ```
    Replace `[file-name]` with the name of the file.

6. **Search for a pattern in a file:**
    ```bash
    grep [pattern] [file-name]
    ```
    Replace `[pattern]` with the pattern you want to search for and `[file-name]` with the name of the file.

## PowerShell (Windows)

1. **Print the current directory:**
    ```powershell
    Get-Location
    ```

2. **Create a new file:**
    ```powershell
    New-Item [file-name]
    ```
    Replace `[file-name]` with the name of the file you want to create.

3. **Open a file using the default editor:**
    ```powershell
    Invoke-Item [file-name]
    ```
    Replace `[file-name]` with the name of the file you want to open.

4. **Show the top of a file's contents:**
    ```powershell
    Get-Content [file-name] -Head 10
    ```
    Replace `[file-name]` with the name of the file.

5. **Show the bottom of a file's contents:**
    ```powershell
    Get-Content [file-name] -Tail 10
    ```
    Replace `[file-name]` with the name of the file.

6. **Search for a pattern in a file:**
    ```powershell
    Select-String -Path [file-name] -Pattern [pattern]
    ```
    Replace `[pattern]` with the pattern you want to search for and `[file-name]` with the name of the file.



## Known Issues and Limitations

1. **Image Storage:** As of now, the application does not support storing generated images. It only stores the URLs of the generated images. To save an image, you need to manually download it from the displayed URL. This limitation is planned to be addressed in future updates.

2. **Django Server:** The application currently runs on the Django development server, which is not meant for production use. For a production environment, it is recommended to use a production-grade server like Gunicorn or uWSGI.

3. **Limited Model Configurations:** The application supports a limited set of configurations for the GPT models. In future updates, we plan to support more configuration options to provide more flexibility to the users.

## Contributing

We welcome contributions to this project. If you want to contribute, please fork the repository, make your changes, and submit a pull request. We will review it and merge your changes.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or suggestions, feel free to open an issue on this repository or reachout at chjthomps@gmail.com.

## Acknowledgements

Thanks to OpenAI for providing the GPT models and the API.
