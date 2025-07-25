from openai import OpenAI
import base64

client = OpenAI(
  api_key="ADD YOUR API KEY HERE",
)

response = client.responses.create(
    model="gpt-4.1",
    input="Generate a personalized offer for Nike running shoes"
)

img = client.images.generate(
    model="gpt-image-1",
    prompt="Generate a personalized offer for Nike running shoes",
    n=1,
    size="1024x1024"
)

image_bytes = base64.b64decode(img.data[0].b64_json)
with open("output.png", "wb") as f:
    f.write(image_bytes)

print(response.output_text)