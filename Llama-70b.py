from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = api_key
)

def ask_openai_question(question):
    try:
        completion = client.chat.completions.create(
            model="nvidia/llama-3.1-nemotron-70b-instruct",
            messages=[{"role": "user", "content": question}],
            temperature=0.5,
            top_p=1,
            max_tokens=1024,
            stream=True
        )

        response_text = ""
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                response_text += chunk.choices[0].delta.content
                print(chunk.choices[0].delta.content, end="") 

        return response_text
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

def main():
    while True:
        question = input("\nMau Tanya bang : ")
        
        if question.lower() == "stop":
            print("Aplikasi dihentikan.")
            break
        
        answer = ask_openai_question(question)
        print("\nJawaban:", answer)

if __name__ == "__main__":
    main()
