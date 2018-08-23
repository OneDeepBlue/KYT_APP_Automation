# coding:utf-8

import requests
import unittest
import ddt
from libs.new_token import new_token

@ddt.ddt
class UpdateTest(unittest.TestCase):
    url="http://183.62.96.187:8855/api/json"
    test_data = '../cases/update_app_tc.yml'

    @ddt.file_data(test_data)
    @ddt.unpack
    def test1_update_app(self,data,message_ass):

        datas = new_token(userno="ZMCS",password="123456",data=data)#更新token信息
        req = requests.post(url=self.url, data=datas)
        message = req.json()['message']
        # print req.text
        self.assertEqual(message, message_ass, '测试失败，返回信息不是%s'%message_ass)

if __name__ == '__main__':
    unittest.main()