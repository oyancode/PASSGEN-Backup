from flask import Flask, render_template
import requests
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/menu')
def menu():
    return render_template('/menu.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    words = requests.get('https://random-word-api.herokuapp.com/word?number=10').json()
    symbols = ['$','&','#','@','!','*']
    passwords = []

    for word in words:
        symbol = random.choice(symbols)
        number = random.randint(100, 999)
        password = word + symbol + str(number)
        passwords.append(password)

    return render_template('menu.html', passwords=passwords)

if __name__ == '__main__':
    app.run(debug=True)