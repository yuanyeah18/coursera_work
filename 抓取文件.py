# -*- coding:utf-8 -*-
import requests
import pandas as pd
import time

headers =  {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

user_data = []
# 创建空字典用于存储数据
def get_user_data(yemian):
    # 定义函数，用于翻页
    for i in range(yemian):
        url = "http://www.zhihu.com/api/v4/members/tinafever/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20".format(i*20)
        response = requests.get(url, headers=headers).json()['data']
        user_data.extend(response)  # 把response数据添加进user_data
        print('正在爬取第%s页' % str(i + 1))
        time.sleep(1)  # 设置爬取网页的时间yemian间隔为1秒

if __name__ == "__main__":
    get_user_data(9)
    df = pd.DataFrame.from_dict(user_data)
    df.to_csv("zhihufoller.csv")
