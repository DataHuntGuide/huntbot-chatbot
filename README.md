# HuntBot Chatbot

A FastAPI-based chatbot that provides hunting regulations using OpenAI's GPT-4o.

## Features

- Answers state-specific hunting questions
- Uses OpenAI GPT-4o
- Detailed formatting and disclaimers
- Web-based frontend

## Setup

1. Create a `.env` file from `.env.template` and paste your OpenAI API key.
2. Run the server:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

3. Open `index.html` in your browser to test.
