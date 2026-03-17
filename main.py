from google import genai
import config

client = genai.Client(api_key=config.api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Cual es la mision de Google?"
)

print(response.text)