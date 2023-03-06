from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/poema1')
def poema1():
    return render_template('poema1.html')



if __name__ == '__main__':
    app.run(debug=True)