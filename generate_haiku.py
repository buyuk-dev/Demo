import os
import random
import requests

# Retrieve environment variables
base_url = os.getenv("AZURE_OPENAI_BASE_URL")
api_key = os.getenv("AZURE_OPENAI_API_KEY")

# Validate environment variables
if not base_url or not api_key:
    raise ValueError("Both AZURE_OPENAI_BASE_URL and AZURE_OPENAI_API_KEY environment variables must be set.")

# Define a random topic
random_topics = ["nature", "technology", "love", "life", "friendship", "wisdom", "time"]
topic = random.choice(random_topics)

# Create a prompt for generating a haiku
prompt = f"Write a haiku about {topic} with words of wisdom."

# Call the Azure OpenAI completions endpoint
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

data = {
    "prompt": prompt,
    "max_tokens": 60,  # Adjust for haiku length
    "temperature": 0.7,  # Creativity level
    "model": "gpt-4-32k"
}

response = requests.post(f"{base_url}/openai/deployments/gpt-4/completions", json=data, headers=headers)

if response.status_code == 200:
    result = response.json()
    haiku = result['choices'][0]['text'].strip()
    print("Generated Haiku:")
    print(haiku)
else:
    print("Failed to generate haiku:", response.text)