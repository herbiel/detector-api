#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：detector-api 
@File    ：call.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/21 6:51 下午 
'''

import queue
import threading
from fs import command
import time

from  sql import update_data


def call(q):
    while True:
        if q.empty():
            return
        else:
            number = q.get()
            cmd = 'originate sofia/internal/sip:%s@192.168.50.16:5080 sleep:5000,hangup inline'%number
            e = command(cmd)
            if e:
                result = e.getBody()
            if 'OK' in result:
                update_data(number, '1')
            else:
                update_data(number, '2')
            time.sleep(5)

def process_call(number_list):
    q = queue.Queue()
    for i in number_list:
        q.put(i)
    thread_num = 20
    threads = []

    for i in range(thread_num):
        t = threading.Thread(target=call, args=(q,))
        threads.append(t)

    for i in range(thread_num):
        threads[i].start()
    for i in range(thread_num):
        threads[i].join()