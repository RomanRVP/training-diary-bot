import os
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
