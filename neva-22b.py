
import requests, base64
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY_NEVA')

invoke_url = "https://ai.api.nvidia.com/v1/vlm/nvidia/neva-22b"
stream = True

with open("assets/images/image.jpg", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode()

assert len(image_b64) < 180_000, \
  "To upload larger images, use the assets API (see docs)"

headers = {
  "Authorization": "Bearer "+ api_key,
  "Accept": "text/event-stream" if stream else "application/json"
}

payload = {
  "messages": [
    {
      "role": "user",
      "content": f'Deskripsikan apa yang kamu lihat di gambar ini, dengan estimasi jaraknya dari saya. <img src="data:image/png;base64,{image_b64}" />'
    }
  ],
  "max_tokens": 1024,
  "temperature": 0.20,
  "top_p": 0.70,
  "seed": 0,
  "stream": stream
}

response = requests.post(invoke_url, headers=headers, json=payload)

if stream:
    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))
else:
    print(response.json())
