import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

## You need a token from https://hf.co/settings/tokens, ensure that you select 'read' as the token type. If you run this on Google Colab, you can set it up in the "settings" tab under "secrets". Make sure to call it "HF_TOKEN"
os.environ["HF_TOKEN"]=os.getenv("HF_TOKEN")

client = InferenceClient("meta-llama/Llama-3.3-70B-Instruct")

def get_weather(location):
    return f"the weather in {location} is sunny with low temperatures. \n"

prompt="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
Answer the following questions as best you can. You have access to the following tools:

get_weather: Get the current weather in a given location

The way you use the tools is by specifying a json blob.
Specifically, this json should have an `action` key (with the name of the tool to use) and a `action_input` key (with the input to the tool going here).

The only values that should be in the "action" field are:
get_weather: Get the current weather in a given location, args: {"location": {"type": "string"}}
example use :

{{
  "action": "get_weather",
  "action_input": {"location": "New York"}
}}

ALWAYS use the following format:

Question: the input question you must answer
Thought: you should always think about one action to take. Only one action at a time in this format:
Action:

$JSON_BLOB (inside markdown cell)

Observation: the result of the action. This Observation is unique, complete, and the source of truth.
... (this Thought/Action/Observation can repeat N times, you should take several steps when needed. The $JSON_BLOB must be formatted as markdown and only use a SINGLE action at a time.)

You must always end your output with the following format:

Thought: I now know the final answer
Final Answer: the final answer to the original input question

Now begin! Reminder to ALWAYS use the exact characters `Final Answer:` when you provide a definitive answer. 
<|eot_id|><|start_header_id|>user<|end_header_id|>
What's the weather in London ?
<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""

# First get the initial thought and action
initial_output = client.text_generation(
    prompt,
    max_new_tokens=200,
    stop=["Observation:"]
)

# Get weather observation
weather_observation = get_weather('London')

# Combine prompt, initial output and observation
new_prompt = prompt + initial_output + f"Observation: {weather_observation}"

# Get final answer
final_output = client.text_generation(
    new_prompt,
    max_new_tokens=200,
)

print(final_output)