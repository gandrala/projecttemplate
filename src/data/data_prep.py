import os
from dotenv import find_dotenv, load_dotenv

print("First dataset loaded")
print("Second dataset about to load")

dotenv_path = find_dotenv()
print(dotenv_path)
load_dotenv(dotenv_path)

print(os.getenv("api_key"))
print(os.getenv("password"))
