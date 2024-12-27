#Class or Functions wherein we make http method calls:
import requests
import json

def get_request(url,auth):
    response=requests.get(url=url,auth=auth)
    return response.json()


def post_request(url,auth,in_json):
    post_response=requests.post(url=url,headers=headers, auth=auth, data=json.dumps(payload))
    if in_json==True:
        return post_response.json()
    return post_response
    

