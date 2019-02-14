import os
from pathlib import Path  
 
import requests

try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser


from pathlib import Path
 

def get_config():
    client_id = os.environ.get("IMGUR_API_ID")
    client_secret = os.environ.get("IMGUR_API_SECRET")
    refresh_token = os.environ.get("IMGUR_REFRESH_TOKEN")

    config = ConfigParser.SafeConfigParser()
    config_path = Path.home().joinpath(".config/imgur_uploader.cfg")
    config.read( config_path )

    try:
        imgur = dict(config.items("imgur"))
    except:
        imgur = {}

    client_id = client_id or imgur.get("id")
    client_secret = client_secret or imgur.get("secret")
    refresh_token = refresh_token or imgur.get("refresh_token", "")

    if not (client_id and client_secret):
        return {}

    data = {"id": client_id, "secret": client_secret}
    if refresh_token:
        data["refresh_token"] = refresh_token
    return data


def imgur_uploader(img_path, id, secret) :
    api_host = 'https://api.imgur.com/3/image'
    headers = { 
    'Authorization' : f'Client-ID {id} Bearer {secret}'
    }
    with open(img_path,'rb') as img :
        files = {'image': img}
        response = requests.post(api_host, files=files, headers=headers)
        #print(response.status_code)
        if response.status_code == 200:
            return { "success" : True, "data": response.json().get("data")}
        else :
            return {"success" : False}
