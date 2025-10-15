import requests
import json
import hashlib

def request():   
    url = "http://0.0.0.0:8000"
    data = {}
    with open('../cs-qualif-step2-bruno/bruno.json', 'r') as file:
        data = json.load(file)

    x = requests.post(url, data)

    if(x.status_code == 200):
        deviceId = (x.json["deviceId"])
        if(len(deviceId) == 32):
            print(1)

if __name__ == "__main__":
    request()
