import pandas as pd  #pip install pandas
from flask import Flask, render_template #pip install flask
from dnacentersdk import DNACenterAPI
from dotenv import dotenv_values
import urllib3
urllib3.disable_warnings()


def get_catalyst_center_data():
    config = dotenv_values(".env_dnac")
    if config.get('verify' == 'False'):
        config['verify'] = False

    dnac = DNACenterAPI(

        username=config['username'],
        password=config['password'],
        base_url=config['base_url'],
        verify=False
    )
    devices = dnac.devices.get_device_list()
    device_list=devices.response

    if not device_list:
        print(f"No devices found")
    else:
        rows =[]
        for device in device_list:
            rows.append({
                "Hostname":device.hostname,
                "Platform":device.platformId,
                "IP":device.managementIpAddress
            })
        df=pd.DataFrame(rows)
    return df
    # print(f"{df}")

app = Flask(__name__)
@app.route('/')
def index():
    data=get_catalyst_center_data()
    data=data.to_html(classes='table table-striped',
                      header="True",index=False)
    return render_template('index.html',table_html=data)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
    
  
