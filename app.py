from flask import Flask
from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv('SECRET_KEY')

# Set up the model and prompt
# consider the speed vs quality models
model_engine = "text-ada-001"
prompt = "Hello, how are you today?"

app = Flask(__name__)

# Generate a response
# completion = openai.Completion.create(
#     engine=model_engine,
#     prompt=prompt,
#     max_tokens=512,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )

@app.route('/')
def hello():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
