import urllib.request
import re
import os
from bs4 import BeautifulSoup

page_flag = 0
base_url = "https://www.169tp.com/xingganmeinv/"
first_url = "https://www.169tp.com/xingganmeinv/list_1_1.html"
imgNums = 0

def get_html(url):
    reponse = urllib.request.urlopen(url)
    html = reponse.read().decode('gb18030')
    return html

def get_imgeurl_list(html):
    img_urlList = re.findall('src=["\']{1}(.+?\.jpg)["\']{1}', html)
    return img_urlList

def download(img_urlList, page_flag, final_path, imgNums):
    num = 1
    for imgurl in img_urlList:
        imgName = "{}{}{}{}.jpg".format(final_path, page_flag, '_', num)
        try:
            urllib.request.urlretrieve(imgurl, imgName)
            print("已经爬取图片名：", imgName)
            imgNums += 1
            num += 1
        except TimeoutError as identifier:
            print("网络超时，请检查网络情况")
            continue

def makedir(path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        print("创建了路径为 ", path, "的文件夹")
        os.makedirs(path)
        return True
    else:
        print("路径为 ", path, "文件夹已存在")
        return False

filepath = input("请输入保存图片的文件夹路径：")
print(filepath)
name = input("请输入保存图片的文件夹名: ")
print(name)
finalpath = filepath + name
makedir(finalpath)
finalpath += '\\'
print(f"图片保存路径：{finalpath}")

download(get_imgeurl_list(first_url), page_flag, finalpath, imgNums)
mysoup = BeautifulSoup(get_html(first_url), 'html.parser')
next_page = mysoup.find('div', attrs = {'class':'page'}).find('li', text='下一页').find('a')
while next_page:
    new_url = base_url + next_page['href']
    page_flag += 1
    download(get_imgeurl_list(get_html(new_url)), page_flag, finalpath, imgNums)
    mysoup = BeautifulSoup(get_html(new_url), 'html.parser')
    next_page = mysoup.find('div', attrs = {'class':'page'}).find('li', text='下一页').find('a')
print(f"下载完成，共下载了 {imgNums} 张图片!")