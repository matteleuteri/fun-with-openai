import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
  prompt="An oil painting of the Massachusetts state house in the reain",
  n=2,
  size="1024x1024"
)

image_url = response['data'][0]['url']

print(image_url)
