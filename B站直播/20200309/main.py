import requests
from bs4 import BeautifulSoup
import time

class PPT():

    def __init__(self):
        self.url = "http://www.51pptmoban.com/ppt/"
        self.host = "http://www.51pptmoban.com"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        }
        self.total = 0

    def getTotal(self):
        """
        获取总页数
        """
        req = requests.get(self.url, headers = self.header)
        req.encoding = "gb2312"
        soup = BeautifulSoup(req.text, "html.parser")
        
        pages = soup.find("div", attrs={'class':'pages'})
        href = pages.find_all('a')[-1]['href']
        start = href.find("_") + 1
        end = href.find(".")
        page_num = href[start:end]
        
        self.total = page_num

    def getContent(self, url):
        req = requests.get(url, headers = self.header)
        req.encoding = "gb2312"
        soup = BeautifulSoup(req.text, "html.parser")
        pdivs = soup.find_all("div", attrs={'class':'pdiv'})

        for pdiv in pdivs:
            href = pdiv.find("a")['href']
            obj_link = self.host + href
            self.getInfo(obj_link)
            time.sleep(1)

    def getInfo(self, url):
        req = requests.get(url, headers = self.header)
        req.encoding = "gb2312"
        soup = BeautifulSoup(req.text, "html.parser")
        ppt_xz = soup.find('div', attrs={"class":"ppt_xz"})
        dl_link = self.host + ppt_xz.find('a')['href']
        self.DLPPT(dl_link)
    
    def DLPPT(self, url):
        session = requests.session()
        req = session.get(url, headers = self.header)
        req.encoding = "gb2312"
        soup = BeautifulSoup(req.text, "html.parser")
        wz = soup.find("div", attrs={"class":'wz'})
        title = wz.find_all('a')[-1].text
        print(title)
        down = soup.find('div', attrs={'class':'down'})
        href = "http://www.51pptmoban.com/e/DownSys/" + down.find('a')['href'][2:]
        temp_header = self.header
        req = session.get(href, headers = temp_header)

        with open(title + ".zip", 'wb') as f:
            f.write(req.content)


if __name__ == "__main__":
    ppt = PPT()
    ppt.getTotal()
    ppt.getContent(ppt.url) # 爬取第一页
    print("第一页下载完成")
    for i in range(2, int(ppt.total)):
        url = "http://www.51pptmoban.com/ppt/index_{}.html".format(str(i))
        ppt.getContent(url)
        time.sleep(1)
        print("第{}页下载完成。".format(str(i)))


