import os
from dotenv import load_dotenv

#load enviroment variables from .env 
load_dotenv()

#lets get the serper api key
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

if SERPER_API_KEY:
    print("api is loading properly", SERPER_API_KEY[:5]+"..."+ SERPER_API_KEY[-5:])
else:
    print("api is not loading properly")