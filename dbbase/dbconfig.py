#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   dbconfig.py
@Time    :   2021/03/08 17:24:06
@Author  :   jacen-ly
@Version :   1.0.1
@Contact :   jacen_ly@163.com
@License :   (C)Copyright ************
@Desc    :   Python 自学
'''

# here put the import lib

from motor.motor_asyncio import AsyncIOMotorClient

MONGOCONFIG = {"host": "127.0.0.1", "port": 27017, "aotodb": "NLAutoTest"}

MONGOCOLLETIONS = {
    "batch_report": "batch_report",
    "case_execute_deatail": "case_execute_deatail",
    "db_config": "db_config",
    "interface_tmp": "interface_tmp",
    "stakeholders_list": "stakeholders_list",
    "test_case": "test_case",
    "version_demand_list": "version_demand_list",
    "interface_cfg": "InterFaceCfg"
}

REDISCONFIG = {
    "host": 'localhost',
    "port": 6379,
    "minsize": 5,
    "maxsize": 10,
    "retry_num": 3,
    "retry_delay": 5
}

Connection = AsyncIOMotorClient(MONGOCONFIG["host"], MONGOCONFIG["port"])
AUTO_MODB = Connection[MONGOCONFIG["aotodb"]]
