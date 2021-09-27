from util.request import Finavia_request
from dotenv import load_dotenv
import os


# Load .env
load_dotenv("/home/nokka200/python/telegram/env/.env")
APP_ID_FINAVIA = os.getenv("APP_ID_FINAVIA")
APP_KEY_FINAVIA = os.getenv("APP_KEY_FINAVIA")

obj = Finavia_request(APP_ID_FINAVIA, APP_KEY_FINAVIA)
