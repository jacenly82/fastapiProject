#!/usr/bin/env python
# encoding: utf-8
'''
# @File    :   myapp.py
# @Time    :   2021/3/4 15:31
# @Site    :   http://test.com
# @Author  :   jacen-ly
# @Version :   1.0
# @Contact :   jacen_ly@163.com
# @License :   (C)Copyright ************
# @Desc    :   LYAuto
'''

import hashlib
from fastapi import FastAPI, Query, Path 
from fastapi import WebSocket
from basemodel.userModel import UserandCode, UserandPassword

app = FastAPI(title='My FastAPI APP',
              description='提供相关的接口服务，数据',
              version='1.0.0')

members = []
ENCODING = 'utf8'


@app.websocket("/ws")
async def join_chatroom(member: WebSocket, name: str):
    await member.acccpet()
    members.append(member)
    while True:
        msg = await member.receive_text()
        [
            await member.send_text("{}:{}".format(name, msg))
            for member in members
        ]


@app.post("/login")
async def user_login_by_password(user: UserandPassword):
    return {
        'msg': "正在开发中",
        'data': {
            'name': user.name,
            'auth_string':
            hashlib.sha1(user.auth_str.encode(ENCODING)).hexdigest(),
            'code': user.code,
        }
    }


@app.post("/login2")
async def user_login_by_code(user: UserandCode):
    return {
        'msg': "正在开发中",
        'data': {
            'name': user.name,
            'code': user.code,
        }
    }


@app.get("/user/{user_id}/info")
async def get_user_info(user_id: str = Path(..., min_length=32,
                                            max_length=32)):
    pass


@app.get("/userList")
async def get_user_list():
    pass


@app.post("/adduser")
async def add_userinfo():
    pass


@app.put("/modifyuser/{user_id}")
async def modify_user(user_id: str = Path(..., min_length=32, max_length=32)):
    pass


@app.delete("/deleteuser/{user_id}")
async def delete_user(user_id: str = Path(..., min_length=32, max_length=32)):
    pass


@app.patch("/authmodify/{user_id}")
async def modify_user_pass(user_id: str = Path(...,
                                               min_length=32,
                                               max_length=32)):
    pass


@app.patch("/activeuser/{active_token}")
async def active_user(active_token: str = Path(...,
                                               min_length=32,
                                               max_length=32)):
    pass


@app.get("/index")
async def index():
    return {"data": [{"name": "jacen", "info": "质量控制一部"}]}
