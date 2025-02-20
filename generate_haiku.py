import os
import random
import requests

# Retrieve environment variables
base_url = os.getenv("AZURE_OPENAI_BASE_URL")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o")
api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-08-01-preview")

# Validate environment variables
if not base_url or not api_key:
    raise ValueError("Both AZURE_OPENAI_BASE_URL and AZURE_OPENAI_API_KEY environment variables must be set.")

# Define a random topic
random_topics = ["nature", "technology", "love", "life", "friendship", "wisdom", "time"]
topic = random.choice(random_topics)

# Create a prompt for generating a haiku
messages = [
    {"role": "system", "content": "You are a poet who writes short, wise haikus."},
    {"role": "user", "content": f"Write a haiku about {topic} with words of wisdom."}
]

# Call the Azure OpenAI chat completions endpoint
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

data = {
    "messages": messages,
    "max_tokens": 60,  # Adjust for haiku length
    "temperature": 0.7  # Creativity level
}

# Construct the full URL for the API request
url = f"{base_url}/openai/deployments/{deployment_name}/chat/completions?api-version={api_version}"

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    result = response.json()
    haiku = result['choices'][0]['message']['content'].strip()
    print(haiku)
else:
    print("Failed to generate haiku:", response.text)