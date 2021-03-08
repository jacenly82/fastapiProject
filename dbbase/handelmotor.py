#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   handelmotor.py
@Time    :   2021/03/05 12:39:31
@Author  :   jacen-ly
@Version :   1.0
@Contact :   jacen_ly@163.com
@License :   (C)Copyright ************
@Desc    :   Python 自学
'''

# here put the import lib

from typing import List, Dict

from dbconfig import AUTO_MODB, MONGOCOLLETIONS

collection = MONGOCOLLETIONS["interface_cfg"]


async def do_insert_one(document: Dict, collection=collection):
    collection = AUTO_MODB[collection]
    document = document
    result = await collection.insert_one(document)
    print('result %s' % repr(result.inserted_id))


async def do_insert_many(documents: List, collection=collection):
    collection = AUTO_MODB[collection]
    documents = documents
    result = await collection.insert_many(documents)
    print('inserted %d docs' % (len(result.inserted_ids), ))


async def do_find_one(key_value: Dict, collection=collection):
    query_content = key_value
    collection = AUTO_MODB[collection]
    document = await collection.find_one(query_content)
    return document
