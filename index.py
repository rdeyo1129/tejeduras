from flask import Flask, request, render_template, session, url_for
from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv('SECRET_KEY')

model_engine = "text-ada-001"

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

grade = None
topic = None
speaker = None

def chatGPT(flavor, prompt):
    def getCustomPrompt(prompt):
        if flavor == "learn":
            return f"Let's talk about this topic: {topic}. Answer my questions like I'm in grade {grade}. If I change the topic, use my prompt to transition back to the topic at hand. Now respond to this prompt: {prompt}"
        if flavor == "speak":
            return f"Pretend to be {speaker} and answer the rest of my questions like you are them. Answer me like I'm in grade {grade} and by relating my prompt to your experience and story. Now respond to my prompt: {prompt}"
        if flavor == "quiz":
            return f"Give me a 6 question quiz on this topic: {topic}. Make the difficulty as if I were in grade {grade}. Give me 3 chances, respond to the first two wrong answers with a hint and then give me the answer on the third wrong guess, then move on to the next question. Give me friendly praise once I've finished the quiz."
        
    response = openai.Completion.create(
        engine=model_engine,
        prompt=getCustomPrompt(prompt),
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.4,
        top_p=0.9,
    )

    text = response.choices[0].text.strip()
    return text

# @app.before_request
# def clear_session():
#     if request.path != url_for('topic'):
#         # Clear the session data except for the csrf_token
#         csrf_token = session.get('csrf_token', None)
#         session.clear()
#         session['csrf_token'] = csrf_token

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topics')
def topics():
    global grade 
    grade = request.args.get('grade')
    return render_template('topics.html', grade=grade)

@app.route('/learn')
def learn():
    global topic
    topic = request.args.get('topic').split(', ')[0]
    return render_template('learn.html', topic=topic)

@app.route('/send-prompt', methods=['POST'])
def submit_form():
    prompt = request.form['user-prompt']
    response = chatGPT("learn", prompt)
    return response

@app.route('/speak')
def speak():
    return render_template('speak.html')

@app.route('/post-speaker')
def submit_speaker():
    global speaker
    speaker = request.form['speaker-radio']

@app.route('/prompt-speaker', methods=['POST'])
def ask_speaker():
    prompt = request.form['prompt-speaker']
    response = chatGPT("speak", prompt)
    return response

@app.route('/quiz-me', methods=['POST'])
def quiz_me():
    response = chatGPT("quiz", prompt="")
    return response

if __name__=='__main__':
    app.run(debug = True)