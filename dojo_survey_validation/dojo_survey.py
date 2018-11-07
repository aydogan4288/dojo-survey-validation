
from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    session['name']= request.form['name']
    session['comment']= request.form['comment']
    if len(request.form['name'])<1:
        flash("A name must be provided")
    if len(request.form['comment'])<1:
        flash("A comment must be provided")
    elif len(request.form['comment']) >120:
        flash("A comment cannot have more than 120 characters")
    else:
        flash("Thanks!")
        return redirect('/')





    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)