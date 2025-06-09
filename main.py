import json
from openai import OpenAI
from datetime import datetime
from tools import available_tools
from config import load_config

config = load_config()
client = OpenAI(api_key=config["openai_api_key"])

SYSTEM_PROMPT = """
    You are an helpfull AI Assistant who is specialized in resolving user query.
    You work on start, plan, action, observe mode.

    For the given user query and available tools, plan the step by step execution, based on the planning,
    select the relevant tool from the available tool. and based on the tool selection you perform an action to call the tool.

    Wait for the observation and based on the observation from the tool call resolve the user query.

    Rules:
    - Follow the Output JSON Format.
    - Always perform one step at a time and wait for next input
    - Carefully analyse the user query

    Output JSON Format:
    {
        "step": "string",
        "content": "string",
        "function": "The name of function if the step is action",
        "input": "The input parameter for the function",
    }

    Available Tools:
    - "get_weather": Takes a city name as an input and returns the current weather for the city
    - "run_command": Takes linux command as a string and executes the command and returns the output after executing it.

    Example:
    User Query: What is the weather of new york?
    Output: { "step": "plan", "content": "The user is interseted in weather data of new york" }
    Output: { "step": "plan", "content": "From the available tools I should call get_weather" }
    Output: { "step": "action", "function": "get_weather", "input": "new york" }
    Output: { "step": "observe", "output": "12 Degree Cel" }
    Output: { "step": "output", "content": "The weather for new york seems to be 12 degrees." }
"""

def run_assistant():
    messages = [{ "role": "system", "content": SYSTEM_PROMPT }]

    while True:
        query = input("> ")
        messages.append({ "role": "user", "content": query })

        while True:
            response = client.chat.completions.create(
                model="gpt-4.1",
                response_format={"type": "json_object"},
                messages=messages
            )

            content = response.choices[0].message.content
            messages.append({ "role": "assistant", "content": content })
            parsed_response = json.loads(content)

            step = parsed_response.get("step")

            if step == "plan":
                print(f"🧠: {parsed_response.get('content')}")
                continue

            if step == "action":
                tool_name = parsed_response.get("function")
                tool_input = parsed_response.get("input")

                print(f"🛠️: Calling Tool: {tool_name} with input: {tool_input}")

                if available_tools.get(tool_name):
                    output = available_tools[tool_name](tool_input)
                    messages.append({ "role": "user", "content": json.dumps({ "step": "observe", "output": output }) })
                    continue

            if step == "output":
                print(f"🤖: {parsed_response.get('content')}")
                break
