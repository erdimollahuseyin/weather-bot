# Weather Information Agent

This project is a Python-based agent that leverages OpenAI's GPT-3.5-Turbo model to interact with users and provide responses about the weather. The agent can fetch the current weather for a specific city and engage in a dialog with the user by executing available actions such as fetching weather data.

## Features

- `Interactive Dialog:` The agent responds to user queries about the weather, running through a thought-action-pause-observation loop.
- `Weather Fetching:` The agent uses an external API (WeatherAPI) to fetch real-time weather data for a given city.
- `OpenAI GPT Integration: The agent leverages OpenAI's GPT-4 model to process user queries and generate intelligent responses.
- `Customizable: The agent's behavior and available actions can be easily modified and extended.

## Setup

#### Development Environment Setup

- Python 3.12.4
- VS Code(or any other code editor)

#### Installation

```bash
$ git clone git@github.com:erdimollahuseyin/weather-bot.git
$ cd weather-bot
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

#### Environment Variables

To run this project, you need to set up two environment variables:

- `WEATHER_API_KEY`: Your API key for WeatherAPI to fetch the weather data.
- `OPENAI_API_KEY`: Your API key for OpenAI to interact with the GPT model.

Create a .env file in the project root directory and add your keys:

```ìni
WEATHER_API_KEY=your_weather_api_key
OPENAI_API_KEY=your_openai_api_key
```

#### Run

```bash
$ python weather_bot.py
```

#### Example Usage

1. The agent initializes and starts listening for user input.
2.It then runs through the thought-action-pause-observation loop to generate responses.
3. If a user asks for the weather in a specific city, the agent fetches the weather using the get_weather function and returns the result.

The script prompts for the maximum number of interactions (turns) before exiting. You can type questions such as:

- "What is the weather like in Istanbul today?"

The agent will output the current weather in the specified city.

#### Example Interaction

```bash
Enter the maximum number of turns: 20
You: What is the weather like in Istanbul today?
Thought: I need to find the current weather report for Istanbul to answer the question accurately.  
Action: get_weather: Istanbul  
PAUSE
 -- running get_weather Istanbul  
Observation: The weather in Istanbul   is 4.4°C with Partly cloudy.
Answer: The weather in Istanbul today is 4.4°C with partly cloudy skies.
```
