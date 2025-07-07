import os
from dotenv import load_dotenv

env = os.getenv('ENVIRONMENT')

dotenv_path = '.env'

load_dotenv(dotenv_path=dotenv_path)

DATABASE_URL = os.getenv('DATABASE_URL')
BROKER_URL = os.getenv('BROKER_URL')