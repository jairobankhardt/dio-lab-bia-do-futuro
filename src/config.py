import os
from dotenv import load_dotenv
from pathlib import Path

# garante que o .env seja encontrado corretamente
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o-mini"