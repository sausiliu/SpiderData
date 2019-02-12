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
    # print(html)
    # text = re.compile()
    soup = BeautifulSoup(html, "lxml")
    # print(soup.prettify())
    # print(soup.body)
    print("-------------------------------------")
    print("dl:")
    # print(soup.dl)
    center = soup.find('dl', class_='text-center', id='fanBox')
    print(center)
    fan = int(center.find('span', id="fan").get_text())
    print("fans:", fan)

    # print(soup.title.name)
    # print(soup.title.string)
    # print(soup.prettify())


    # for p_tag in soup.find_all('p'):
    #     if p_tag.has_attr('class'):
    #         print(p_tag['class'])
    print("-------------------------------------")

    print(soup.select('.read'))
