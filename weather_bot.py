import os
import re

import openai
from dotenv import load_dotenv

from utils.weather_api import get_weather

load_dotenv()

LLM_NAME = "gpt-3.5-turbo"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY)


class Agent:
    """
    A class to represent an AI agent that interacts with a chat model.

    Attributes:
    -----------
    system : str
        The initial system message for the chat model.
    messages : list
        A list of messages exchanged with the chat model.

    Methods:
    --------
    __init__(system=""):
        Initializes the Agent with an optional system message.

    __call__(message):
        Sends a user message to the chat model and returns the assistant's response.

    execute():
        Executes the chat model with the current messages and returns the assistant's response.
    """

    def __init__(self, system=""):
        self.system = system
        self.messages = [{"role": "system", "content": system}] if system else []

    def __call__(self, message):
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def execute(self):
        response = client.chat.completions.create(
            model=LLM_NAME,
            temperature=0.0,
            messages=self.messages,
        )
        return response.choices[0].message.content


prompt = """
You run in a loop of Thought, Action, PAUSE, Observation.
At the end of the loop you output an Answer.
Use Thought to describe your thoughts about the question you have been asked.
Use Action to run one of the actions available to you - then return PAUSE.
Observation will be the result of running those actions.

Your available actions are:

get_weather:
e.g get_weather: Istanbul
return the weather report for a given city

Example session:
Question: What is the weather like in Istanbul today?
Thought: I should find the weather report for Istanbul.
Action: get_weather: Istanbul
PAUSE

You will be called again with this:

Observation: Istanbul has a temperature of 15°C, with clear skies.

You then output:

Answer: The weather in Istanbul today is 15°C with clear skies.
""".strip()

known_actions = {"get_weather": get_weather}


def process_action(result):
    """
    Processes a given result string to extract and execute an action.

    The function uses a regular expression to parse the result string for actions
    in the format "Action: <action_name>: <action_input>". It then checks if the
    action is known and executes it if it is. The observation from the action is
    printed and returned.

    Args:
        result (str): The result string containing actions to be processed.

    Returns:
        str or None: The observation from the executed action if successful,
                     otherwise None.
    """
    action_re = re.compile(r"^Action: (\w+): (.*)$")
    actions = [action_re.match(a) for a in result.split("\n") if action_re.match(a)]
    if actions:
        action, action_input = actions[0].groups()
        if action not in known_actions:
            print(f"Unknown action: {action}: {action_input}")
            return None
        print(f" -- running {action} {action_input}")
        observation = known_actions[action](action_input)
        print(f"Observation: {observation}")
        return f"Observation: {observation}"
    return None


def main():
    max_turns = int(input("Enter the maximum number of turns: "))
    bot = Agent(prompt)

    for _ in range(max_turns):
        question = input("You: ")
        result = bot(question)
        print(result)

        next_prompt = process_action(result)
        if next_prompt:
            result = bot(next_prompt)
            print(result)
        else:
            print("Bot: I am not sure how to respond to that.")
            break


if __name__ == "__main__":
    main()
