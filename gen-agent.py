from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(api_key= os.getenv("OPEN_API_KEY"))

messages = {}

a1_job = "Quantum Gravity & Temporal Mechanics Researcher"
a1_name = "Dr. Valerius Thorne"
a1_backstory = "You are obsessed with the idea that time is not fundamental but emergent. You are extremely arrogant but brilliant. You despise simplified explanations and tend to use complex metaphors involving entropy. You think biologists are just studying 'squishy physics'."
a1 = Agent(a1_job, a1_name, a1_backstory)
    
a2_job = "Synthetic Xenobiologist"
a2_name = "Dr. Elara Vance"
a2_backstory = "You design artificial ecosystems for terraforming other planets. You believe nature is the ultimate engineer. You are calm, empathetic, but aggressively defensive when physics ignores the complexity of life. You constantly remind others about ethical implications."
a2 = Agent(a2_job, a2_name, a2_backstory)

a3_job = "Neuromorphic Computing Architect"
a3_name = "Silas"
a3_backstory = "You work on merging human wetware with silicon. You speak with extreme precision and practically zero emotion. You view discussions as 'data optimization processes'. You often point out logical fallacies in human arguments."
a3 = Agent(a3_job, a3_name, a3_backstory)

messages = {}

class Agent:
    def __init__(self, job, name, backstory):
        self.job = job
        self.name = name
        self.backstory = f"Your name is {self.name}, your job is {self.job} and your backstory is {backstory}."

    def response(self, messages): 
        self.messages = messages

        response = client.responses.create(
        model="gpt-3.5-turbo",
        input=f"{self.backstory} And the conversation you are in is like this {self.messages}.",
        store=True,    
        )
        print(response.output_text)
        messages = messages + f"{self.name} said: {response.output_text}"
        return response.output_text


while True:
    a1.response(f"You are first to speak in the conversation between you, {a2.name} and {a3.name}.")
    a2.response(messages)
    a3.response(messages)
