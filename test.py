from dotenv import load_dotenv
load_dotenv()

import os

print("API Key:", os.getenv("GOOGLE_API_KEY"))
