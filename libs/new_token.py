# coding:utf-8


from libs.user_token import user_token
import json


def new_token(userno=None,password=None,data=None):
    t = user_token(userno=userno, password=password)  # 获取token
    # 将获取到的token信息更新到请求的data中
    datas = data
    head = data['head']
    token = json.loads(head)
    token['token'] = t
    datas['head'] = json.dumps(token)
    return datas
