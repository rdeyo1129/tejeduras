from flask import Flask, request, render_template
 
# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topics')
def topics():
    value = request.args.get('grade')
    return f"The value you entered was {value}."
    # return render_template('topics.html')

# @app.route('/page2')
# def page2():

 
if __name__=='__main__':
    app.run(debug = True)