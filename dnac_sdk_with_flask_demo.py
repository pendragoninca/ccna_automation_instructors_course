import pandas as pd  #pip install pandas
from flask import Flask, render_template #pip install flask
from dnacentersdk import DNACenterAPI
from dotenv import dotenv_values
import urllib3
urllib3.disable_warnings()

app = Flask(__name__)

def get_catalyst_center_data():
    config = dotenv_values(".env_dnac")
    if config.get('verify' == 'False'):
        config['verify'] = False

  
@app.route('/')
def index():

if __name__ == "__main__":
    app.run(debug=True,port=5000)
    
  
