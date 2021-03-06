import ssl
import matplotlib
from urllib import request
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties

from pylab import mpl

from matplotlib.font_manager import _rebuild
_rebuild() #reload一下

# font = FontProperties(fname='./SimHei.ttf')
print(matplotlib.Path())
print(matplotlib.get_data_path() )
print(matplotlib.get_configdir() )
print(matplotlib.matplotlib_fname())
print(mpl.font_manager.get_cachedir())

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

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
    # print("dl:")
    # print(soup.dl)

    # for center in soup.find_all('dl', class_='text-center'):
        #print(center)

    center = soup.find('dl', class_='text-center', id='fanBox')
    # print(center)

    fan_str = center.find('span', id="fan").get_text()
    fan = int(fan_str)

    # print("-------------------------------------")
    # print(fan_str)
    # print("fans:", fan)

    # print(soup.title.name)
    # print(soup.title.string)
    # print(soup.prettify())

    # for p_tag in soup.find_all('p'):
    #     if p_tag.has_attr('class'):
    #         print(p_tag['class'])
    print("-------------------------------------")

    mainBox = soup.body.find('div', id="mainBox")  # mainBox has main, aside, script ...
    article_list = mainBox.main.find('div', class_='article-list')

    labels_list = []
    val_list = []

    for article in article_list.find_all('div', class_='article-item-box csdn-tracking-statistics'):
        article_name = article.h4.a.get_text()
        article_name = article_name.strip().\
            replace('\n', '').replace(' ', '')
        num_info = article.find('div', class_='info-box d-flex align-content-center')

        # print(num_info)
        read_info = num_info.find('span', class_='num')
        if read_info is None:
            continue

        read_num = int(read_info.get_text())
        # print(article_name)
        # print(read_num)
        labels_list.append(article_name)
        val_list.append(read_num)
        # print('')

    # print(mainBox.main.prettify())
    # print(labels_list)
    # print(val_list)
    vals = [1, 2, 3, 4]  # 创建数据系列
    fig, ax = plt.subplots()  # 创建子图
    labels = 'A', 'B', 'C', 'D'
    # colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    # explode = (0, 0.1, 0, 0)
    # ax.pie(val_list, explode=explode, labels=labels_list, colors=colors,
    ax.pie(val_list, labels=labels_list, autopct='%1.1f%%', shadow=True, startangle=90, radius=1.2)
    ax.set(aspect="equal", title='xxxxxx')  # 设置标题以及图形的对称
    plt.show()

