from smolagents import CodeAgent, tool,LiteLLMModel
from dotenv import load_dotenv
load_dotenv()

# Tool to suggest a menu based on the occasion

@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion (str): The type of occasion for the party. Allowed values are:
                        - "casual": Menu for casual party.
                        - "formal": Menu for formal party.
                        - "superhero": Menu for superhero party.
                        - "custom": Custom menu.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."

# Alfred, the butler, preparing the menu for the party
agent = CodeAgent(tools=[suggest_menu], model=LiteLLMModel(model_id="gemini/gemini-2.0-flash"))

# Preparing the menu for the party
agent.run("Prepare a formal menu for the party.")

agent.push_to_hub('ViktorJJF/AlfredAgent')