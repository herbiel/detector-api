#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：detector-api 
@File    ：sql.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/20 5:57 下午 
'''

##数据库detector-call

import pymysql
import time
import uuid
conn = pymysql.connect(
    host='192.168.50.25',
    port=3306,
    user='tangbull',
    passwd='tangbull',
    db='detector-call'
)

def insert_data(taskid,numberlist):
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    uuid_str = uuid.uuid4()
    for number in numberlist:
        sql = 'INSERT INTO record(task_id,number,idle,create_time,uuid) VALUES("%s""%s","%s","%s")' %(taskid,number, "True",create_time,uuid_str)
        cur = conn.cursor()
        cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()

