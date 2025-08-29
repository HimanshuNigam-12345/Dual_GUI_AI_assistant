# AI Assistant Project

This project is a versatile AI assistant accessible through both a command-line interface (CLI) and a web-based application. It uses the OpenRouter API to perform various tasks, including answering questions, summarizing text, and generating creative content. The application is designed with a modular structure, separating the user interfaces from the shared core logic.

## Features

- **Dual Interfaces**: Choose between a fast command-line tool and a user-friendly web interface.
- **Multiple Functions**:
  - **Q&A**: Get answers to your questions.
  - **Summarization**: Condense long articles or documents.
  - **Creative Content**: Generate ideas, poems, or story hooks.
- **Conversation History**: All interactions with the AI are automatically logged in `conversation_history.json`.
- **Feedback Collection**: Users can rate the helpfulness of AI responses, and the feedback is stored in `feedback.json`.
- **Modular Codebase**: The core AI logic and prompts are shared between the CLI and web app, ensuring consistency and maintainability.

## Configuration and Setup

Follow these steps to configure and run the project.

### 1. API Key Setup

This project requires an API key from OpenRouter.

1.  Go to [OpenRouter.ai](https://openrouter.ai/), sign up, and get your free API key.
2.  Set the API key as an environment variable named `OPENAI_API_KEY`. On Windows PowerShell, you can do this with the `setx` command. **Replace `"YOUR_API_KEY_HERE"` with your actual key.**

    ```powershell
    setx OPENAI_API_KEY "YOUR_API_KEY_HERE"
    ```

3.  **Important**: After running `setx`, you must close and reopen your terminal or Visual Studio Code for the new environment variable to be loaded.

### 2. Install Dependencies

The project requires Python packages listed in `requirements.txt`.

1.  Make sure you have Python and pip installed.
2.  Open your terminal in the project's root directory (`internship/`).
3.  Run the following command to install the necessary packages:

    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Assistant

You can run either the command-line or the web version of the assistant.

### To Run the CLI Version:

1.  Navigate to the CLI directory:
    ```bash
    cd ai_assistant_cli
    ```
2.  Run the assistant script:
    ```bash
    python assistant.py
    ```

### To Run the Web App Version:

1.  Navigate to the web app directory:
    ```bash
    cd ai_assistant_web
    ```
2.  Run the Flask application:
    ```bash
    python app.py
    ```
3.  Open your web browser and go to `http://127.0.0.1:5000`.

## Output Files

The application will create the following files in the root `internship` directory:

- `conversation_history.json`: A log of all prompts and the AI's responses.
- `feedback.json`: A log of all feedback submitted by users.
