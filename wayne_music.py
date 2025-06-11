from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel
from dotenv import load_dotenv

load_dotenv()

agent = CodeAgent(tools=[DuckDuckGoSearchTool()],model=LiteLLMModel(model_id="gemini/gemini-2.0-flash"))

print(agent.run("Search for the best music recommendations for a party at the Wayne's mansion."))