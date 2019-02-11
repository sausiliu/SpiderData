import re
import ssl
from urllib import request
from bs4 import BeautifulSoup

context = ssl._create_unverified_context()
url = "https://blog.csdn.net/richard_liujh"

if __name__ == "__main__":
    response = request.urlopen(url, context=context)
    # 可以使用chardet.detect()来监测网页的编码格式
    html = response.read().decode('utf-8')
    #print(html)
    #text = re.compile()
    soup = BeautifulSoup(html, "lxml")
    print(soup)
