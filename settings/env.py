"""Module containing the configuration for the application"""
import os
from dotenv import load_dotenv

load_dotenv()

def get_string_env(key: str):
    """Gets a value from the environment variables. Throws an error if the variable is not set."""
    value = os.getenv(key)

    if value is None or value == "":
        raise Exception(f"{key} environment variable not defined or empty.")

    return value

JWT = get_string_env("AUTHORIZATION_JWT")
URL = get_string_env("GRAPQHL_URL")
