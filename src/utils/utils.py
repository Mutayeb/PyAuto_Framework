# class or functions:
def common_headers_json(self):
    headers={
        "Content_Type":"Äpplication/json"
        }
    return headers

def common_headers_xml(self):
    headers={
        "Content_Type":"Äpplication/xml"
        }
    return headers


def common_headers_put_patch_delete_basic_auth():
    headers={
        "Content-Type":"Application/json",
        "Authorization":"Basic YWRtaW46cGFzc3dvcmQxMjM="
    }
    return headers

def header_put_patch_del_cookie(token):
    headers={
        "Content-Type":"Application/json",
        "Cookie":"Token="+str(token)
    }
    return headers

def read_scv_file():
    pass
def read_env_var_file():
    pass

util=Utils.common_headers_json()