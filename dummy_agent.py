import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

## You need a token from https://hf.co/settings/tokens, ensure that you select 'read' as the token type. If you run this on Google Colab, you can set it up in the "settings" tab under "secrets". Make sure to call it "HF_TOKEN"
os.environ["HF_TOKEN"]=os.getenv("HF_TOKEN")

client = InferenceClient("meta-llama/Llama-3.3-70B-Instruct")
# if the outputs for next cells are wrong, the free model may be overloaded. You can also use this public endpoint that contains Llama-3.2-3B-Instruct
# client = InferenceClient("https://jc26mwg228mkj8dw.us-east-1.aws.endpoints.huggingface.cloud")

output = client.text_generation(
    "The capital of France is",
    max_new_tokens=100,
)

print(output)