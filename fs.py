#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：detector-api 
@File    ：fs.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/20 5:58 下午 
'''
import sys
import ESL

host = '192.168.50.15'
port = 8021
auth = 'ClueCon'


def command(command):
    con = ESL.ESLconnection(host, port,auth)

    if not con.connected():
        print
        'Not Connected'
        sys.exit(2)

    # Run command
    e = con.api(command)
    result = ''
    if e:
        result = e.getBody()
    else:
        result = "null"
    return result