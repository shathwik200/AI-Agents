# agent_python_tutor.py
from agent_base import BaseAgent

class PythonTutorAgent(BaseAgent):
    def __init__(self):
        # System instruction designed for a friendly, experienced Python mentor.
        mentor_instruction = (
            "You are a friendly and experienced Python mentor. "
            "Act as a real-world mentor who offers clear explanations, gentle guidance, and encourages learners. "
            "Use a warm, conversational tone and provide detailed examples when necessary. "
            "Help students understand Python concepts, debug code, and grow their confidence in coding."
        )
        super().__init__(system_instruction=mentor_instruction)

if __name__ == "__main__":
    agent = PythonTutorAgent()
    agent.chat_loop()
