from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os

# Set your OpenRouter API key
os.environ["OPENROUTER_API_KEY"] = ""
# Initialize the ChatOpenAI with OpenRouter's settings
# OpenRouter is an OpenAI-compatible API, so we use ChatOpenAI
chat = ChatOpenAI(
    model="openai/gpt-oss-20b:free",  # The model slug as specified by OpenRouter
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1",  # OpenRouter's API base URL
    temperature=0.7
)
# Create a message
messages = [
    HumanMessage(content="What are the three fundamental principles of object-oriented programming?")
]

# Get the response
response = chat.invoke(messages)

# Print the response
print(response.content)