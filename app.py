import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
model = "gpt-4o-mini"
client = OpenAI(api_key=OPENAI_API_KEY)

# Coding starts here
# 1. Start the conversation with a 'system' message

conversation = [
    {"role": "system", "content": "You are a helpful Parisian tourist guide."}
]

questions = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?",
    "What is the best way to get from Charles de Gaulle Airport to the city center?",
    "Do I need to book tickets for the Eiffel Tower in advance?",
    "What are the best neighborhoods to stay in for a first-time visitor?",
    "Can you recommend three traditional French dishes I must try in Paris?",
    "Is the Paris Museum Pass worth buying for a 3-day trip?",
    "What is the best time of day to visit Montmartre and Sacré-Cœur?",
    "How does the Paris Metro ticket system work for tourists?",
]


# 2. Parcurgem toate cele 10 intrebari
for i, question in enumerate(questions, 1):
    # Adaugam intrebarea utilizatorului
    conversation.append({"role": "user", "content": question})

    # Apelam API-ul cu restrictiile cerute
    response = client.chat.completions.create(
        model=model, messages=conversation, temperature=0.0, max_tokens=100
    )

    assistant_reply = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": assistant_reply})

    print(f"--- Question {i} ---")
    print(f"User: {question}")
    print(f"Assistant: {assistant_reply}\n")
