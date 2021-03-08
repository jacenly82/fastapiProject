#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   userModuel.py
@Time    :   2021/03/08 12:44:31
@Author  :   jacen-ly
@Version :   1.0
@Contact :   jacen_ly@163.com
@License :   (C)Copyright ************
@Desc    :   Python 自学
'''

# here put the import lib

from typing import Optional
from pydantic import BaseModel, EmailStr, FilePath
from enum import Enum, IntEnum


class ActiveEnum(IntEnum):
    notactive = 0
    active = 1
    locked = 2
    member = 5
    cancel = 8
    quit = 9


class CompanyEnum(str, Enum):
    nlsoftware_fj = '福建新大陆软件工程有限公司'


class UserandPassword(BaseModel):
    # name必填项
    name: str
    # auth_str必填项
    auth_str: str
    # code必填项
    code: str
    # is_save_cookie,description可选项
    is_save_cookie: bool = False


class UserandCode(BaseModel):
    # name必填项
    name: str
    # code必填项
    code: str
    # is_save_cookie可选项
    is_save_cookie: bool = False


class UserInfo(BaseModel):
    '''
    classname: UserInfo 基本类型校验
    description: 对用户数据基本类型校验
    properties: {user_id:str 字符串类型，由后台统一生成的自定义uuid,
           auth_str:str sha1值, email:EmailStr 邮箱类型字符串}
    return:{*}
    '''
    user_id: str
    auth_str: str
    email: EmailStr
    user_name: str = None
    nick_name: str = None
    contact: str = None
    address: str = None
    company: CompanyEnum = CompanyEnum.nlsoftware_fj
    is_active: ActiveEnum = ActiveEnum.notactive
    description: Optional[str]
    head_imag: FilePath = None
