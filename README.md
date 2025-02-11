# Python Mentor

**Python Tutor Mentor** is an interactive, AI-powered Python tutoring agent designed to guide users through Python programming concepts, debugging, and core topics with clear examples—all within an engaging chat-based interface. Built using the Groq API, this tool maintains session history, provides context-aware responses, and uses an object-oriented design for easy customization and scalability.

Whether you're a beginner learning Python or an experienced developer looking for quick guidance, Python Tutor Mentor is here to help!

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Interactive Chat:** Engage in a two-way conversation with a friendly Python mentor.
- **Session History:** Maintains full conversation context to provide accurate and personalized guidance.
- **Friendly Mentor Tone:** Designed to be warm, empathetic, and encouraging—just like a real-world mentor.
- **Modular Design:** Separated configuration, base functionality, and specialized agent code for clarity and scalability.
- **Customizable Responses:** Easily extend or modify the system instructions to tailor the mentor's behavior.
- **Debugging Assistance:** Helps users debug their Python code with step-by-step explanations and suggestions.


## Project Structure

The project is organized into modular components for clarity and maintainability:

```
python-tutor-mentor/
├── config.py               # Initializes the Groq API client with your API key.
├── agent_base.py           # Base agent class managing session history and the interactive loop.
└── agent_python_tutor.py   # Python Tutor Mentor agent with system instructions for friendly mentoring.
```


## Installation

### Prerequisites

Before getting started, ensure you have the following installed:

- Python 3.8 or higher
- [Groq Python Client](https://pypi.org/project/groq/)
- A valid Groq API key

### Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/shathwik200/Python-Mentor-AI-Agent.git
   cd python-tutor-mentor
   ```

2. Set up a virtual environment:
   - On macOS/Linux:
     ```bash
     python -m venv env
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv env
     env\Scripts\activate
     ```

3. Install dependencies:
   ```bash
   pip install groq
   ```

4. Set your Groq API key:
   - On macOS/Linux:
     ```bash
     export GROQ_API_KEY="your_api_key_here"
     ```
   - On Windows (Command Prompt):
     ```cmd
     set GROQ_API_KEY="your_api_key_here"
     ```

5. Run the Python Tutor Mentor:
   ```bash
   python agent_python_tutor.py
   ```


## Usage

Once the application is running, you can interact with the Python Tutor Mentor in a conversational manner. Here's an example interaction:

```plaintext
You: How do I define a function in Python?
Mentor: In Python, you define a function using the `def` keyword. For example:

    def greet(name):
        return f"Hello, {name}!"

This function takes a parameter `name` and returns a greeting. Let me know if you have any questions!
```

Feel free to ask questions about Python syntax, debugging, best practices, or anything else related to programming!

---

## Contributing

We welcome contributions from the community! Whether you want to fix a bug, add a feature, or improve documentation, your help is appreciated. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them with clear messages:
   ```bash
   git commit -m "Add feature XYZ"
   ```
4. Push your changes to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Submit a pull request with a detailed description of your changes.

For major changes, please open an issue first to discuss what you'd like to change.

---

## Code of Conduct

We are committed to fostering an open and welcoming environment. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to understand the expectations for participating in this project.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## Contact

If you have any questions, feedback, or need support, feel free to reach out:

- Open an issue in the repository.
- Email: shathwik200@gmail.com

---

Enjoy your journey in learning Python with your friendly mentor! 🚀
