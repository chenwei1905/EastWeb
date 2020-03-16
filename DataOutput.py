#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import requests
import re
from multiprocessing import Pool
import csv
import pandas as pd
import os
import time

# 默认路径地址
filePath = "D:\\scriptproject\\python\\EastWeb\\data\\"
if not os.path.exists(filePath):
    os.mkdir(filePath)
os.chdir(filePath);

def write_header(data,tablename):
    with open('{}.csv'.format(tablename), 'a', encoding="utf_8_sig", newline='') as f:
        # headers = list(data[0].keys())
        print(data) #测试OK
        writer = csv.writer(f)
        writer.writerow(data);

def write_table(data, page, tablename):
    print("\n 正在下载写入第 %s 页表格" % page)
    # 写入文件的方法
    for d in data:
        with open('{}.csv'.format(tablename), 'a', encoding='utf_8_sig', newline='') as f:
            w = csv.writer(f)
            w.writerow(d.values())

def writeTableFromList(data, page, tablename):
    print("\n 正在下载写入第 %s 页表格" % page)
    # 写入文件的方法
    for d in data:
        with open('{}.csv'.format(tablename), 'a', encoding='utf_8_sig', newline='') as f:
            w = csv.writer(f)
            w.writerow(d)

def readTableFromCsv(fileName):
    lst = []
    with open(fileName, 'r', encoding='utf8' ) as fp:
        lst = [i for i in csv.reader(fp)]  # csv.reader 读取到的数据是list类型
    return lst

if __name__ == "__main__":

    tablename = "test"
 


    datanew = [[1,2], [4,5]]
    writeTableFromList(datanew,1, tablename)



