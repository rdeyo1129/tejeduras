from flask import Flask
from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv('SECRET_KEY')

# Set up the model and prompt
# consider the speed vs quality models
# model_engine = "text-davinci-003" or ada?
prompt = "Hello, how are you today?"

app = Flask(__name__)

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

@app.route('/')
def hello():
    return prompt

if __name__ == '__main__':
    app.run(debug=True)

# However, OpenAI does offer a free tier that allows you to make up to 100,000 API requests per month for free. If your personal project stays within this limit, you can use the API at no cost.