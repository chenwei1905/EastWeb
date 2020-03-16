#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json


class URLManage(object):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    def __init__(self, url, data):
        self.url = url
        self.data = data

    def get(self):
        try:
            r = requests.get(self.url, params=self.data, headers=self.header).text
            #r.encoding = 'utf-8'
            #json_r = r.json()
            print("Get请求结果:", r)
            return r
        except BaseException as e:
            print("请求失败!", str(e))

    def post(self):
        try:
            r = requests.post(self.url, data=self.data, headers=self.header).text
            #r.encoding = 'utf-8'
            #json_r = r.json()
            print("Post执行结果：", r)
            return r
        except BaseException as e:
            print("请求失败!", str(e))


if __name__ == "__main__":
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    params = {
        'fid': 'f3',
        'pi': 0,
        'pz': 40,
        'po': 1,
        'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
        'fltt': 2,
        'fields': 'f14,f12,f13,f2,f3,f4,f6,f104,f105,f106',
        'np': 1,
        'cb': 'jQuery1124016769571594629085_1581424226346',
        'secids': '100.TOP40,100.AS51,100.ATX,100.BFX,100.BVSP,100.TSX,100.PX,100.FCHI,100.HEX,100.GDAXI,100.AEX,100.ASE,100.SENSEX,100.ICEXI,100.JKSE,100.N225,100.KS11,100.ISEQ,100.MIB,100.KLSE,100.MXX,100.NZ50,100.KSE100,100.WIG,100.RTS,100.OMXSPI,100.STI,100.CSEALL,100.IBEX,100.SSMI,100.SET,100.TWII,100.FTSE,100.DJIA,100.NDX,100.SPX,100.VNINDEX',
        '_': 1581424226714


    }
    a = URLManage("http://11.push2.eastmoney.com/api/qt/ulist.np/get", params)
    a.get()
    #字符串删除处理
    #print(type(a.get()))
    result = a.get()[a.get().find('(') + 1: a.get().find(')')]
    #print(result)
    state = json.loads(result)
    print("****************")
    print(state.get('rc'))
    print("****************")
    print(state.get('rt'))

