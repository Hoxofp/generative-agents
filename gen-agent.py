from dotenv import load_dotenv
from google import genai
from google.genai import types
import os
import time

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

messages = []

class Agent:
    def __init__(self, job, name, backstory):
        self.job = job
        self.name = name
        self.backstory = f"Your name is {self.name}, your job is {self.job} and your backstory is {backstory}."

    def response(self, messages): 
        self.messages = "\n".join(messages)

        prompt = (
            f"--- IDENTITY ---\n"
            f"Name: {self.name}\n"
            f"Job: {self.job}\n"
            f"Backstory: {self.backstory}\n\n"
            f"--- CONVERSATION HISTORY ---\n"
            f"{self.messages}\n\n"
            f"--- INSTRUCTION ---\n"
            f"You are {self.name}. Reply to the conversation above. "
            f"Do NOT repeat previous messages. Only provide your new response.\n\n"
            f"{self.name}:" 
        )
        response = client.models.generate_content(
            model = "gemini-2.5-flash-lite",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=200,
                stop_sequences=["\nDr. Valerius", "\nDr. Elara", "\nSilas"]
            )
        )
        print(prompt)
        agent_response = response.text.strip()
        print(f"{self.name} said:\n {agent_response}")
        messages.append(f"{self.name} said: {agent_response}")
        time.sleep(4)
        return agent_response



a1 = Agent(
    "Quantum Gravity Researcher", 
    "Dr. Valerius Thorne", 
    "Obsessed with emergent time. Arrogant but brilliant. Uses complex entropy metaphors."
)
    
a2 = Agent(
    "Synthetic Xenobiologist", 
    "Dr. Elara Vance", 
    "Designs artificial ecosystems. Calm, empathetic, defensive about biological complexity."
)

a3 = Agent(
    "Neuromorphic Architect", 
    "Silas", 
    "Merges wetware with silicon. Precise, emotionless, points out logical fallacies."
)

first_message = f"You are first to speak in the conversation between you, {a2.name} and {a3.name}."
messages.append(first_message)

round_counter = 0

while round_counter < 3:
    print(f"\n=== Round {round_counter + 1} ===")
    a1.response(messages)
    a2.response(messages)
    a3.response(messages)

    round_counter = round_counter + 1
