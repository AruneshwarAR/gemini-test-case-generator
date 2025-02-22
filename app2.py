from openai import OpenAI
import os 
client = OpenAI(
api_key=os.getenv("GOOGLE_API_KEY")
, # Replace with your Gemini API key
base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = "gemini-2.0-flash"
response = client.chat.completions.create(
model=model, 
messages=[
{"role": "system", "content": "You are a helpful assistant."},
{
"role": "user",
"content": "Explain to me how AI works"
}],
stream=True
)
for chunk in response:
    print(chunk.choices[0].delta.content, end="")
      