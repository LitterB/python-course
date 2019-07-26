import requests

all_urls = []

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

def run():
    headers = {
        "Host":"www.meizitu.com",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
    }
    #images collection and list rule url
    target_url = 'http://www.meizitu.com/a/pure_%d.html'
    spider = Spider(target_url, headers)
    spider.getUrls(1, 16)
    print(all_urls)

if __name__ == "__main__":
    run()