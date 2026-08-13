# 🤖 AI Agent with Groq & Gemini API

A simple and secure Python-based AI Agent that connects with the **Groq API** (Llama 3.3 model) to provide instant, concise, and expert answers to user queries.

---

## 🌟 Features

* **Secure Configuration:** Environment variables (`.env`) are fully isolated and ignored via `.gitignore` to prevent secret leaks.
* **Smart Environment Loading:** Uses `python-dotenv` to automatically locate and load environment variables.
* **Fast LLM Inference:** Powered by Groq's high-speed `llama-3.3-70b-versatile` model.
* **Interactive Notebook:** Includes a Jupyter Notebook (`Untitled-1.ipynb`) for testing and experimentation.

---

## 📁 Project Structure

```text
my_first_agent/
├── app.py                 # Main Python execution script
├── Untitled-1.ipynb       # Jupyter Notebook for testing & research
├── .env.example           # Template for environment variables
├── .gitignore             # Tells Git which files/folders to ignore
└── README.md              # Project documentation
```

🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

📋 Prerequisites
Ensure you have Python 3.10+ installed on your system.

🛠️ Installation & Setup
Clone the Repository

Bash
git clone [https://github.com/mosha-me/my-first-ai-agent.git](https://github.com/mosha-me/my-first-ai-agent.git)
cd my-first-ai-agent/my_first_agent
Create & Activate Virtual Environment

Linux/macOS:
Bash
python3 -m venv ai_env
source ai_env/bin/activate
Windows:

Bash
python -m venv ai_env
ai_env\Scripts\activate
Install Dependencies
Install the required Python packages:

Bash
pip install groq python-dotenv ipykernel
Configure Environment Variables

Duplicate .env.example and rename it to .env:

Bash
cp .env.example .env
Open the .env file and replace the placeholder with your actual Groq API Key:

Code snippet
GROQ_API_KEY=your_actual_groq_api_key_here
💻 Usage
Run the Main Python Script
To interact with the AI agent via the terminal:

Bash
python app.py
Run via Jupyter Notebook
If you prefer testing step-by-step:

Open VS Code or launch Jupyter:

Bash
jupyter notebook
Open Untitled-1.ipynb and run the code cells sequentially.

🛡️ Security Note
Never commit your actual .env file to public repositories! The .gitignore file included in this repository ensures that secret keys and local virtual environments remain safe and private.

📄 License
This project is open-source and available under the MIT License.
