import requests
import threading
import re
import time

all_urls = []
all_img_urls = []
g_lock = threading.Lock()

class Spider():
    #constract function
    def __init__(self, target_url, headers):
        self.target_url = target_url
        self.headers = headers

    def getUrls(self, start_page, page_num):
        global all_urls
        for i in range(start_page, page_num + 1):
            url = self.target_url % i
            all_urls.append(url)

class Producer(threading.Thread):
    def run(self):
        headers = {
            "Host":"www.meizitu.com",
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
        }
        global all_urls
        while len(all_urls) > 0:
            g_lock.acquire()
            page_url = all_urls.pop()

            g_lock.release()
            try:
                print("分析" + page_url)
                response = requests.get(page_url, headers=headers, timeout=3)
                all_pic_link = re.findall('<a target=\'_blank\' href="(.*?)">', response.text, re.S)
                global all_img_urls
                g_lock.acquire()
                all_img_urls += all_pic_link
                print(all_img_urls)
                g_lock.release()
                time.sleep(0.5)
            except:
                pass

        #images collection and list rule url
        target_url = 'http://www.meizitu.com/a/pure_%d.html'
        spider = Spider(target_url, headers)
        spider.getUrls(1, 16)
        print(all_urls)


if __name__ == "__main__":
    pass