#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   myuuid.py
@Time    :   2021/03/08 15:17:24
@Author  :   jacen-ly
@Version :   1.0
@Contact :   jacen_ly@163.com
@License :   (C)Copyright ************
@Desc    :   Python 自学
'''

# here put the import lib

import uuid
import hashlib


class TempBytes():
    def __init__(self, var: str, encoding='utf-8') -> None:
        self.str = var
        self.bytes = bytes(var, encoding=encoding)


def get_uuid(namespace=None, name=None):
    '''
    name: get_uuid
    description:  由于uuid1 是通过ip mac地址生成，会产生安全问题
                  所以通过uuid1生成的进行md5转后，通过uuid5 生成唯一值
    param: {name : str} name为uuid5需要的一个系统唯一值，不传默认生一个为uuid1的md5值
    return {str} : 返回32位唯一字符串且去掉连接符，确保不会重复 
    '''
    tem_uuid = str(uuid.uuid1())
    # print('uuid.NAMESPACE_DNS：',tem_uuid)
    if not name:
        name = hashlib.md5(tem_uuid.encode()).hexdigest()
    if not namespace:
        namespace = uuid.NAMESPACE_DNS
    else:
        namespace = TempBytes(hashlib.sha1(namespace.encode()).hexdigest())

    uuid_str = str(uuid.uuid5(namespace, name))
    return ''.join(uuid_str.split('-'))


if __name__ == '__main__':
    print(get_uuid())
    print(get_uuid('test_api', 'test'))
