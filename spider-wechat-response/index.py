import requests
from lxml import etree
from bs4 import BeautifulSoup

#获取返回码内容页面
response = requests.get('https://open.weixin.qq.com/cgi-bin/showdocument?action=doc&id=open1419318634&t=0.1833771689889907')
#获取文档内容
response_text = response.text
#初始化并指定解析器
soup = BeautifulSoup(response_text, "lxml")
#获取到table
table = soup.table
#获取所有tr
tr_arr = table.find_all("tr")
#删除第一个无用的tr
del tr_arr[0]
#遍历tr获取td，得到td内容
for tr in tr_arr:
    tds = tr.find_all("td")
    #拼接所需的字符串
    result = "WX_ERROR_RESULT_MAP.put(\"" + tds[0].get_text() + "\", \"" + tds[2].get_text() + "\");"
    #打印数据
    print(result)
