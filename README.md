# 🗼 Paris Travel Planner Chatbot

An AI-powered virtual tourist guide built with Python and the OpenAI API (`gpt-4o-mini`). This project simulates an intelligent travel assistant for **Peterman Reality Tours**, designed to help visitors plan their trip to Paris by answering 10 essential sightseeing, logistics, and cultural questions.

## ✨ Features

* **Multi-Turn Conversation History:** Maintains context across all 10 questions using a structured `system`, `user`, and `assistant` message history (`conversation` list).
* **Deterministic & Concise Responses:** Configured with `temperature=0.0` for factual accuracy and `max_tokens=100` for clear, concise travel advice.
* **Secure API Key Management:** Uses `python-dotenv` to load environment variables securely from a local `.env` file.

## 💬 The 10 Questions Answered

The chatbot automatically processes and answers the following 10 tourist questions:
1. *How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?*
2. *Where is the Arc de Triomphe?*
3. *What are the must-see artworks at the Louvre Museum?*
4. *What is the best way to get from Charles de Gaulle Airport to the city center?*
5. *Do I need to book tickets for the Eiffel Tower in advance?*
6. *What are the best neighborhoods to stay in for a first-time visitor?*
7. *Can you recommend three traditional French dishes I must try in Paris?*
8. *Is the Paris Museum Pass worth buying for a 3-day trip?*
9. *What is the best time of day to visit Montmartre and Sacré-Cœur?*
10. *How does the Paris Metro ticket system work for tourists?*

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **AI Model:** OpenAI `gpt-4o-mini`
* **Libraries:** `openai`, `python-dotenv`

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR-USERNAME/Paris-Travel-Chatbot.git](https://github.com/YOUR-USERNAME/Paris-Travel-Chatbot.git)
cd Paris-Travel-Chatbot
