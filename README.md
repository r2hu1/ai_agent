# 🤖 AI Agent

A step-by-step reasoning AI agent powered by OpenAI's GPT API. It simulates a tool-using assistant that can **plan**, **act**, **observe**, and **respond** to user queries using predefined tools like weather checking and shell command execution.

## ✨ Features

- 🔁 Interactive command-line interface
- 📚 Reasoning based on a planning-action-observation loop
- 🛠️ Tool execution framework with:
  - `get_weather`: Fetch current weather for a city using `wttr.in`
  - `run_command`: Run Linux shell commands securely
- 🌐 Uses OpenAI's GPT API (via `openai` Python client)
- 🔒 Environment variable support via `.env`


## 📁 Project Structure

```txt
ai\_agent/
├── ai\_assistant/
│   ├── **init**.py
│   ├── main.py       # Core agent loop
│   ├── tools.py      # Tool functions like get\_weather, run\_command
│   └── config.py     # OpenAI client and env config
├── run.py            # Entry point
├── .env              # Environment file (add your API key here)
├── requirements.txt  # Project dependencies
└── README.md         # You’re here
```

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/r2hu1/ai_agent.git
cd ai_agent
````

### 2. Set Up Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure `.env`

Create a `.env` file with your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

## 🧠 How It Works

The agent follows a structured reasoning format:

1. **Plan** what to do based on the user query.
2. **Select a tool** (`get_weather`, `run_command`).
3. **Perform an action** using the tool.
4. **Observe** the result.
5. **Respond** to the user based on the output.

Example conversation:

```txt
> What is the weather in Tokyo?
🧠: The user is interested in the weather for Tokyo.
🧠: From the available tools, I should call get_weather.
🛠️: Calling Tool: get_weather with input Tokyo
🤖: The weather in Tokyo is ☀️ +24°C.
```



## 🧩 Future Plans

Maybe upgrade it!
