#!/usr/env/bin
# _*_ coding=utf-8 _*_

import json
import requests

def get_page(page):
    url_temp = 'http://temp.163.com/special/00804KVA/cm_guonei_0{}.js'
    return_list = []
    for i in range(page):
        url = url_temp.format(i)
        response = requests.get(url)
        if response.status_code != 200:
            continue
        content = response.text
        print (content)
    return return_list

get_page(5)

