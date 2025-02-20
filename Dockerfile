# Start with a lightweight Python image
FROM python:3.9-slim

# Set environment variables for Azure OpenAI credentials
ENV AZURE_OPENAI_BASE_URL="" \
    AZURE_OPENAI_API_KEY=""

# Install necessary Python libraries
RUN pip install requests

# Copy the script into the container
COPY generate_haiku.py /app/generate_haiku.py

# Set the working directory
WORKDIR /app

# Define the command to run the script
CMD ["python", "generate_haiku.py"]