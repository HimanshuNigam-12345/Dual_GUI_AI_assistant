import os
import json
from openai import OpenAI
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Centralized client initialization
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Use absolute paths to ensure files are always saved in the same place
FEEDBACK_FILE = os.path.join(BASE_DIR, "feedback.json")
HISTORY_FILE = os.path.join(BASE_DIR, "conversation_history.json")

def save_interaction(user_input, ai_output, history_file="conversation_history.json"):
    """Saves the user input and AI output to a history file."""
    history_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_input": user_input,
        "ai_output": ai_output
    }
    
    history_dir = os.path.dirname(history_file)
    if history_dir and not os.path.exists(history_dir):
        os.makedirs(history_dir)

    try:
        if os.path.exists(history_file) and os.path.getsize(history_file) > 0:
            with open(history_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
        else:
            history = []
    except (json.JSONDecodeError, FileNotFoundError):
        history = []

    history.append(history_entry)
    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

def get_ai_response(prompt):
    """Gets a response from the AI and saves the interaction."""
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. "
                    "Do not show reasoning steps, analysis, or thought process. "
                    "Only return the final answer in plain text, with proper newlines."
                ),
            },
            {"role": "user", "content": prompt}
        ],
    )
    raw_response = completion.choices[0].message.content
    cleaned_response = clean_output(raw_response)
    
    # Save the interaction
    save_interaction(prompt, cleaned_response)
    
    return cleaned_response

def clean_output(text: str) -> str:
    if "assistantfinal" in text:
        text = text.split("assistantfinal", 1)[-1]
    elif "Final Answer:" in text:
        text = text.split("Final Answer:", 1)[-1]
    return text.strip()

def save_feedback(func, prompt_text, helpful, note=""):
    entry = {"function": func, "prompt": prompt_text, "helpful": helpful, "note": note}
    data = []
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = [] # File was empty or corrupt
    
    data.append(entry)
    with open(FEEDBACK_FILE, "w") as f:
        json.dump(data, f, indent=2)