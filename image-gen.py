import os
import openai
import dotenv
import webbrowser

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
  prompt="A bengal cat rolling around in the grass.",
  n=1,
  size="1024x1024"
)

image_url = response['data'][0]['url']

print(image_url)
webbrowser.open_new_tab(image_url)
