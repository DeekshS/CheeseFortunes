
#from flask import Flask, render_template

#app = Flask(__name__)

#@app.route('/')
#def index():
    #return render_template('index.html')

#if __name__ == '__main__':
    #app.run(debug=True)

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
