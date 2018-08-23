# coding:utf-8

import requests
import json
from libs.shareModules import genearteMD5

def user_token(userno="simon",password='1'):
    #获取用户token(默认simon账号)
    pa = genearteMD5(password)#将密码转换MD5（16位）
    url = "http://183.62.96.187:8855/api/json"
    data = {
        "head": '{"appid":"KYTESTDRV","command":"StaffLogin","device_id":"F30000370000E1","encrypt_type":0,"sign":"66da9672e0ff00d2","token":"","version":"1.1"}',
        "body": '{"datainfo":null,"password":"%s","userno":"%s"}'%(pa,userno)
    }
    try:
        req = requests.post(url=url, data=data)
        body = req.json()['body']
        token = json.loads(body)['token']
        return token
        # print token
    except Exception :
        print req.text


if __name__ == '__main__':
     t = user_token(userno='ZMCS',password='123456')
     print t
