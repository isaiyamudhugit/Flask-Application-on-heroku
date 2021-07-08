from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "<h1>This is flask application. working on heroku cloud platform</h1>"

if  __name__ == "__main__":
    app.run()

