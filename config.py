import os

import dotenv

dotenv.load_dotenv()

POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
