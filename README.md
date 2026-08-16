# 🤖 Discord AI Chatbot

## Introduction:

Discord AI Chatbot is an AI-powered Discord bot built using **Python**, **Discord.py**, and **Google GenAI**. The bot allows users to interact with an AI directly through Discord by mentioning the bot in a message.

The project is designed as a simple and practical example of integrating **Discord Bot APIs with Google's Gemini AI models**, making it easy to build an intelligent conversational assistant inside a Discord server.

## Features:

### 🤖 AI-Powered Chat:

* Responds to users when the Discord bot is mentioned.
* Uses Google's GenAI API to generate intelligent responses.
* Supports natural-language conversations directly inside Discord.
* Sends AI-generated responses back to the Discord channel.

### 💬 Discord Integration:

* Built using the Discord.py library.
* Supports asynchronous Discord event handling.
* Automatically detects when the bot is mentioned.
* Provides a simple and lightweight Discord chatbot experience.

### 🔐 Environment Variables:

* Discord bot token is stored securely using environment variables.
* Google API key is stored securely using environment variables.
* Uses `.env` configuration with `python-dotenv`.
* Sensitive credentials are excluded from GitHub using `.gitignore`.

### 🧠 Google Gemini:

* Uses Google's GenAI SDK for AI-generated responses.
* Sends user messages to the configured Gemini model.
* Returns the generated response directly to Discord.

## Tech Stack:

**Programming Language:** Python

**Discord Library:** Discord.py

**AI SDK:** Google GenAI

**AI Model:** Google Gemini

**Environment Management:** python-dotenv

**Configuration:** `.env`

## Project Structure:

```text
Discord-AI_BOT/
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

> ⚠️ The `.env` file is used locally and should **never be uploaded to GitHub**, as it contains private API credentials.

## Installation:

### Clone the repository:

```bash
git clone https://github.com/HibaNaveed/Discord-AI-Chatbot.git
```

### Navigate to the project directory:

```bash
cd Discord-AI-Chatbot
```

### Create a virtual environment:

```bash
python -m venv venv
```

### Activate the virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

Or install the required packages manually:

```bash
pip install discord.py python-dotenv google-genai
```

## Environment Variables:

Create a `.env` file in the root directory of the project:

```env
discord_secret_key=YOUR_DISCORD_BOT_TOKEN
google_api_key=YOUR_GOOGLE_API_KEY
```

Replace the placeholder values with your actual credentials.

**Never share or commit these credentials publicly.**

## Discord Bot Setup:

To use the chatbot, you first need to create a Discord application and bot.

1. Create an application in the Discord Developer Portal.
2. Add a bot to your application.
3. Copy the Discord bot token.
4. Add the token to your `.env` file.
5. Enable the **Message Content Intent**.
6. Invite the bot to your Discord server.
7. Make sure the bot has permission to read and send messages.

The application uses the Message Content Intent:

```python
intents = discord.Intents.default()
intents.message_content = True
```

## Google GenAI Setup:

Create a Google AI API key and add it to your `.env` file:

```env
google_api_key=YOUR_GOOGLE_API_KEY
```

The application loads the key using `python-dotenv`:

```python
load_dotenv()

google_key = os.getenv("google_api_key")
```

The Google GenAI client is then initialized using the API key:

```python
client_google = genai.Client(api_key=google_key)
```

## How It Works:

The bot first connects to Discord using the Discord bot token.

When a user mentions the bot, the `on_message` event detects the message:

```python
if client.user in message.mentions:
```

The user's message is then sent to Google's GenAI API:

```python
interaction = client_google.interactions.create(
    model="gemini-3.6-flash",
    input=message.content
)
```

The generated response is sent back to the Discord channel:

```python
await message.channel.send(interaction.output_text)
```

## Running the Bot:

After configuring your `.env` file, start the bot using:

```bash
python main.py
```

If the bot connects successfully, the console will display:

```text
We have logged in as <bot name>
```

You can then mention the bot in your Discord server:

```text
@YourBot Hello, how are you?
```

The bot will process your message using the configured Google Gemini model and return the AI-generated response.

## Example:

**User:**

```text
@AI-Bot What is artificial intelligence?
```

**Bot:**

```text
Artificial intelligence is a field of computer science focused on
creating systems that can perform tasks that normally require
human intelligence, such as understanding language, learning,
reasoning, and problem solving.
```

## API and Data Sources:

### Discord API:

Used to connect the application to Discord, receive messages, detect mentions, and send AI-generated responses.

### Google GenAI API:

Used to process user messages and generate AI responses using Google's Gemini models.

### Environment Variables:

Used to securely store the Discord bot token and Google API key without hardcoding credentials into the source code.

## Security:

Sensitive credentials should never be included directly in the source code.

The project uses a `.env` file:

```env
discord_secret_key=YOUR_DISCORD_BOT_TOKEN
google_api_key=YOUR_GOOGLE_API_KEY
```

The `.env` file should be included in `.gitignore`:

```gitignore
.env
.env.*
__pycache__/
*.pyc
```

If a Discord bot token or Google API key is accidentally exposed, immediately revoke or rotate the affected credential.

## Future Improvements:

* Add conversation history and context.
* Add Discord slash commands.
* Add AI system prompts and customizable personalities.
* Add typing indicators while generating responses.
* Add error handling for API failures.
* Add moderation commands.
* Add configurable AI models.
* Add chat history storage.
* Add administrator configuration commands.
* Add support for multiple AI providers.

## Contribution:

We welcome contributions!

If you have suggestions, bug reports, feature requests, or improvements, feel free to:

* Open an issue.
* Submit a pull request.
* Suggest new features.
* Improve the documentation.

Before submitting a pull request, please make sure that no API keys, Discord tokens, `.env` files, or other sensitive credentials are included.

## License:

This project is licensed under the **MIT License**, allowing you to freely use, modify, and distribute the software under the terms of the license.

## 📌 Repository:

GitHub: [HibaNaveed/Discord-AI-Chatbot](https://github.com/HibaNaveed/Discord-AI-Chatbot?utm_source=chatgpt.com)
