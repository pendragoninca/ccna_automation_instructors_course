from ncclient import manager #pip install ncclient
import xml.dom.minidom
from dotenv import dotenv_values
from os import environ

def get_running_config():

    with manager.connect(host=HOST,
                            port=PORT,
                            username=USER,
                            password=PASS,
                            hostkey_verify=False,
                            device_params={'name': 'iosxe'},
                            look_for_keys=False,
                            allow_agent=False) as m:

        print(f"Calling to {HOST}...")
        response = m.get_config(source='running')
        xml_doc = xml.dom.minidom.parseString(response.data_xml)
    print(xml_doc.toprettyxml(indent="  "))

if __name__ == '__main__':
    config=dotenv_values(".env_sandbox")
    HOST = config['host']
    PORT = config['port']
    USER = config['username']
    PASS = config['password']
    get_running_config()