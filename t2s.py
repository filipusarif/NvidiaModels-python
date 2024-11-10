import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY_T2S')

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/9BWtsMINqrJLrRacOk9x" 

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": api_key
}

data = {
  "text": "hola i'm arif",
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.75,  
    "similarity_boost": 0.8  
  }
}

response = requests.post(url, json=data, headers=headers)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
