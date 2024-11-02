import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the API key
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

if API_KEY is None:
    raise ValueError("API key not found. Please set the ALPHA_VANTAGE_API_KEY environment variable.")