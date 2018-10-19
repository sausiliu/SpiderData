import re
import ssl
from urllib import request
context = ssl._create_unverified_context()

if __name__ == "__main__":
    response = request.urlopen("https://blog.csdn.net/richard_liujh", context=context)
    # 可以使用chardet.detect()来监测网页的编码格式
    html = response.read().decode('utf-8')
    print(html)
    text = re.com
    print('hello world')