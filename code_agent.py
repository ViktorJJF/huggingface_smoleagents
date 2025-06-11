import subprocess
from smolagents import CodeAgent,DuckDuckGoSearchTool, HfApiModel,load_tool,tool,LiteLLMModel
import datetime
import requests
import pytz
import yaml
from tools.final_answer import FinalAnswerTool
from dotenv import load_dotenv

load_dotenv()

@tool
def open_file(filename: str) -> str:
    """
    Open a file.
    Args:
        filename: The name of the file to open.
    """
    return open(filename, 'r').read()

@tool
def execute_python_code(code: str) -> str:
    """
    Execute python code.
    Args:
        code: The python code to execute.
    """
    return subprocess.run(code, shell=True, capture_output=True, text=True).stdout

@tool
def make_http_request(url: str, method: str, headers: dict, body: dict) -> str:
    """
    Make an HTTP request to a given URL.
    Args:
        url: The URL to make the request to.
        method: The HTTP method to use (e.g., 'GET', 'POST').
        headers: A dictionary of headers to include in the request.
        body: A dictionary of the request body.
    """
    try:
        response = requests.request(method, url, headers=headers, json=body)
        return response.text
    except Exception as e:
        return f"Error making HTTP request: {str(e)}"

# Below is an example of a tool that does nothing. Amaze us with your creativity !
@tool
def write_file(filename: str, content: str) -> str: #it's import to specify the return type
    #Keep this format for the description / args / args description but feel free to modify the tool
    """Writes content to a file.  Creates the file if it doesn't exist, overwrites if it does.
    Args:
        filename: The name of the file to write to (e.g., 'my_file.txt').  Include the extension.
        content: The text content to write to the file.
    Returns:
        A message indicating success or failure.
    """
    try:
        with open(filename, 'w') as f:  # 'w' mode for writing (overwrites)
            f.write(content)
        return f"Successfully wrote content to file: {filename}"
    except Exception as e:
        return f"Error writing to file {filename}: {str(e)}"


@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """A tool that fetches the current local time in a specified timezone.
    Args:
        timezone: A string representing a valid timezone (e.g., 'America/New_York').
    """
    try:
        # Create timezone object
        tz = pytz.timezone(timezone)
        # Get current time in that timezone
        local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"The current local time in {timezone} is: {local_time}"
    except Exception as e:
        return f"Error fetching time for timezone '{timezone}': {str(e)}"


final_answer = FinalAnswerTool()


# Import tool from Hub
image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True)

with open("prompts.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)
    
agent = CodeAgent(
    tools=[final_answer,get_current_time_in_timezone,write_file,make_http_request,execute_python_code,open_file], ## add your tools here (don't remove final answer)
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    prompt_templates=prompt_templates,
    additional_authorized_imports=['open', 'bs4','os'],
    model=LiteLLMModel(model_id="gemini/gemini-2.0-flash")
)


print(agent.run("crea un nuevo archivo llamado 'test.txt' y escribe 'Hola mundo' en el archivo dentro de la carpeta the directory, no te di el nombre exacto porsiaca tienes que buscarlo. Elabora un plan primero para buscarlo y luego para escribir en el archivo"))