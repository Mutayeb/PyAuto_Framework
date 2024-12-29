# class or functions:
class Util(object):

    def common_headers_json(self):
        headers={
        "Content-Type": "application/json"
        }
        return headers

    def common_headers_xml(self):
        headers={
            "Content_Type":"application/xml"
        }
        return headers


    def common_headers_put_patch_delete_basic_auth():
        headers={
        "Content-Type":"application/json",
        "Authorization":"Basic YWRtaW46cGFzc3dvcmQxMjM="
    }
        return headers

    def header_put_delete_patch_cookie(self, token):
        headers={
        "Content-Type":"application/json",
        "Cookie":"Token="+str(token)
    }
        return headers

    def read_scv_file():
        pass
    def read_env_var_file():
        pass

#util=Utils.common_headers_json()