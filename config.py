from dotenv import load_dotenv
import os

def load_config():
    load_dotenv()
    return {
        "openai_api_key": os.getenv("OPENAI_API_KEY")
    }
