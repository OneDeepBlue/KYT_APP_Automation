# coding:utf-8

import hashlib

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# 类名称：genearteMD5
# 类的目的：将字符串md5加密
# 假设：无
# 影响：无
# 输入：需要转换的字符串
# 返回值：16位md5字符串
# 创建者：lingy
# 创建时间：2018/8/21
# 修改者：
# 修改原因：
# 修改时间:
#-------------------------------------------------------------------------------
def genearteMD5(str):
    # 创建md5对象
    hl = hashlib.md5()

    # Tips
    # 此处必须声明encode
    # 否则报错为：hl.update(str)    Unicode-objects must be encoded before hashing
    hl.update(str.encode(encoding='utf-8'))

    return hl.hexdigest()[8:-8]#生成16位md5字符串
    # print('MD5加密前为 ：' + str)
    # print('MD5加密后为 ：' + hl.hexdigest()[8:-8])
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    genearteMD5('1')