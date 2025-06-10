# Hugging Face Agents Project

This project contains examples of using Hugging Face models as agents for various tasks.

Its just for Fun and learning

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/huggingface_smoleagents.git
    cd huggingface_smoleagents
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your Hugging Face Token:**
    You need a token from [https://hf.co/settings/tokens](https://hf.co/settings/tokens). Ensure that you select 'read' as the token type.
    Set the `HF_TOKEN` environment variable. For example:
    ```bash
    export HF_TOKEN="hf_xxxxxxxxxxxxxx"
    ```
    If you are running this on Google Colab, you can set it up in the "settings" tab under "secrets".

## Usage

### Dummy Agent

The `dummy_agent.py` demonstrates a basic text generation task using a Hugging Face Inference Client.

To run the dummy agent:
```bash
python dummy_agent.py
```

### COT Agent

The `cot_agent.py` likely implements a Chain-of-Thought (COT) agent, which can perform more complex reasoning tasks.

To run the COT agent:
```bash
python cot_agent.py
``` 