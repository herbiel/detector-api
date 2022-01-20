#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：detector-api 
@File    ：main.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/20 5:12 下午 
'''
from typing import Optional

from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from sql import insert_data
import pymysql
import time




app = FastAPI()

class Item(BaseModel):
    number: List[str] = []


@app.post("/detector")
async def detector( item: Item):
    ##存入数据库
    insert_data(item.number)
    ##批量取出识别
    ##结果存入数据库
    return "hello world"