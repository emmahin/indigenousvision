import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis un fichier .env
load_dotenv()

# Accès aux variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# En-têtes pour appel API
OPENAI_HEADERS = {
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}
