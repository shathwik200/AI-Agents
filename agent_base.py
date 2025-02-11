# agent_base.py
from config import client  # Import the shared Groq client from config.py

class BaseAgent:
    def __init__(self, system_instruction: str, model: str = "deepseek-r1-distill-llama-70b"):
        self.system_instruction = system_instruction
        self.model = model
        # Start the conversation history with the system message.
        self.history = [{"role": "system", "content": self.system_instruction}]

    def add_message(self, role: str, content: str):
        """Append a message to the conversation history."""
        self.history.append({"role": role, "content": content})

    def get_response(self) -> str:
        """
        Send the conversation history to the API and return the assistant's reply.
        The reply is also added to the conversation history.
        """
        response = client.chat.completions.create(
            messages=self.history,
            model=self.model,
        )
        assistant_reply = response.choices[0].message.content
        self.add_message("assistant", assistant_reply)
        return assistant_reply

    def chat_loop(self):
        """Run an interactive loop that maintains conversation history until the user types 'exit'."""
        print("Python Tutor Mentor. Type 'exit' to end the session.")
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == "exit":
                print("Goodbye! Keep coding and remember: every mistake is a learning opportunity.")
                break
            self.add_message("user", user_input)
            reply = self.get_response()
            print("Mentor:", reply)
            print()
