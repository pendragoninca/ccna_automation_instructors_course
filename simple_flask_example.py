from flask import Flask
from flask import Flask #pip install flask
from os import environ
from dotenv import load_dotenv #pip install python-dotenv

def get_env_var(env_var):
    return environ[env_var]

app=Flask(__name__)
@app.route('/')
def index():
    print(f"Print to console")
    return f"Hello World"

if __name__ == "__main__":

    app.run(debug=True,port=5000)