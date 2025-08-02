# Professionally Me!

## Overview
Professionally Me! is a personal assistant and profile management tool that leverages AI to interact with users, answer questions, and manage personal data. The project uses OpenAI, Gradio, and other tools to provide a chat-based interface for professional self-presentation and information management.

## Features
- Chat interface powered by Gradio
- Integration with OpenAI for intelligent responses
- PDF and text file processing
- Modular design for easy extension


## Folder Structure
- `app.py`: Main entry point for the application.
- `requirements.txt`: Python dependencies.
- `me/`: Contains user-specific content and profile data.
- `env/`: (Optional) Contains environment variable files or virtual environment data. If present, you may store a `.env` file here with sensitive configuration such as API keys, or use this folder for Python virtual environment files. **Do not commit sensitive data to version control.**
- `prompts/`: Prompt templates for AI interactions.
- `push_notification/`: Notification utilities.
- `tools/`: Tool definitions and utility functions.


## The `me` Folder
The `me` folder is intended to store personal information and profile data for the user. Specifically, it should contain:

- `about_me.txt`: A plain text file with a self-summary or personal introduction. This should be a brief, well-written summary about yourself, your background, and your professional interests.
- `Profile.pdf`: A PDF file containing a saved version of your LinkedIn profile. Export your LinkedIn page as a PDF and place it here. This allows the application to extract and use your professional information for various features.

**Note:** Do not add sensitive information or credentials to this folder. Only include your self-summary and LinkedIn PDF.

## The `env` Folder
The `env` folder is used to store environment-specific files. This may include:

- `.env`: A file containing environment variables such as API keys, secrets, or configuration values required by the application. Example variables:
  - `OPENAI_API_KEY=your_openai_key_here`
  - `GEMINI_URL=your_gemini_url_here`
  - `GEMINI_KEY=your_gemini_key_here`
  - Add PushOver key, user if push notification functionality has to work
- Python virtual environment files (if you use `python -m venv env`).

**Important:**
- Never commit sensitive information (like API keys) to version control.
- Add `env/` or `.env` to your `.gitignore` to keep secrets safe.

## Getting Started
1. Clone the repository.
2. Add your `about_me.txt` and `Profile.pdf` to the `me/` folder.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python app.py
   ```

## License
This project is for personal use. See LICENSE for details.
