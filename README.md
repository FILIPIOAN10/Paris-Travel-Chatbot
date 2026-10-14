# 🗼 Paris Travel Planner Chatbot

An AI-powered virtual tourist guide built with Python and the OpenAI API (`gpt-4o-mini`)[cite: 1, 2]. This project simulates an intelligent travel assistant for **Peterman Reality Tours**, designed to help visitors plan their trip to Paris by answering common sightseeing, logistics, and cultural questions[cite: 2].

## ✨ Features

* **Multi-Turn Conversation History:** Maintains context across multiple questions using a structured `system`, `user`, and `assistant` message history[cite: 2].
* **Deterministic & Concise Responses:** Configured with `temperature=0.0` for factual accuracy and `max_tokens=100` for clear, concise travel advice[cite: 2].
* **Secure API Key Management:** Uses `python-dotenv` to load environment variables securely from a local `.env` file[cite: 1].

## 💬 Sample Questions Answered

The chatbot is pre-configured to answer key tourist questions, including:
1. *How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?*[cite: 2]
2. *Where is the Arc de Triomphe?*[cite: 2]
3. *What are the must-see artworks at the Louvre Museum?*[cite: 2]
*(Plus additional questions covering airport transit, ticket booking, neighborhoods, French cuisine, and the Paris Metro).*

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **AI Model:** OpenAI `gpt-4o-mini`[cite: 1, 2]
* **Libraries:** `openai`, `python-dotenv`[cite: 1]

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR-USERNAME/Paris-Travel-Chatbot.git](https://github.com/YOUR-USERNAME/Paris-Travel-Chatbot.git)
cd Paris-Travel-Chatbot
