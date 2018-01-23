import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/online-registration')
def online_registration():
    return render_template('new.html')


@app.route('/trainers')
def trainers():
    return render_template('trainers.html')


@app.route('/contact-us')
def contact_us():
    return render_template('contacts.html')


@app.route('/plans')
def plans():
    return render_template('plans.html')


@app.route('/facility')
def facility():
    return render_template('facility.html') 


PORT = int(os.environ.get("PORT"))
if __name__ == "__main__":
    app.run("0.0.0.0", port=PORT)
    # app.run('0.0.0.0', 5000)

