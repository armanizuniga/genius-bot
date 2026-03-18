# 🍎 Genius Bar Chatbot

A CLI-based Apple Genius Bar support chatbot powered by Claude AI. 
Ask Armani anything about your Apple devices and get warm, knowledgeable support 
right from your terminal.

## Demo
![Genius Bar Chatbot CLI](assets/demo.png)

## Features
- Conversational memory — Armani remembers context within a session
- Graceful scope handling — stays focused on Apple products and services
- Clean terminal UI powered by `rich`
- Easy session reset without restarting

## Setup

### 1. Clone the repo
git clone https://github.com/armanizuniga/genius-bot.git
cd genius-bot


### 2. Install dependencies
pip install -r requirements.txt

### 3. Add your API key
Create a .env file in the root directory:
ANTHROPIC_API_KEY=your-key-here

### 4. Run the chatbot
python cli.py

## Commands
| Command | Action                  |
|---------|-------------------------|
| reset   | Start a new session     |
| quit    | Exit the chatbot        |

## Project Structure
genius-bar-bot/
├── bot/
│   ├── __init__.py
│   ├── agent.py        
│   └── prompts.py      
├── cli.py              
├── .env                
├── .gitignore
├── requirements.txt
└── README.md

## Built With
- [Anthropic Claude API](https://www.anthropic.com)
- [Rich](https://github.com/Textualize/rich)
- [python-dotenv](https://github.com/theskumar/python-dotenv)


Here's your complete file checklist before running:
```
✅ bot/__init__.py      (empty file)
✅ bot/prompts.py
✅ bot/agent.py
✅ cli.py
✅ .env                 (with your API key)
✅ .gitignore
✅ requirements.txt
✅ README.md
```

Once those are all in place, run:
```
pip install -r requirements.txt
python cli.py