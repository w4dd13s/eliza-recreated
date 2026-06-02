# Eliza – A Python Remake of the Classic Rogerian Therapist Chatbot

> **Note:** This is an old project I made, but it's still a great way to get a solid grasp of how rule‑based AI systems work under the hood.

ELIZA is one of the first natural language processing programs, developed in the mid‑1960s. This version is a lightweight, beginner‑friendly Python implementation that simulates a psychotherapist using simple pattern matching and substitution rules. 

## Features
- **Rule‑based conversation** – Responds to user input with predefined patterns and templates.
- **Randomized responses** – Adds a natural, less predictable feel.
- **Quit keywords** – Gracefully ends the conversation.
- **Classic ASCII intro** – Displays the iconic ELIZA logo and a short explanation.

## How It Works
1. User input is matched against a list of regular expression patterns (defined in a separate `rules.py` file).
2. The first matching pattern selects a random response template.
3. Captured groups from the regex are inserted into the response using `str.format()`.
4. Special quit keywords (e.g., `bye`, `quit`) trigger a final goodbye message.
