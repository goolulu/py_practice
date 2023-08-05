from typing import Hashable
from urllib import request
import pandas as pd
from requests import request
from bs4 import BeautifulSoup, SoupStrainer


"""
Series
"""

# 声明


def ser_declear():
    hello = pd.Series([1, 2, 3, 4, 5, 6])
    print(hello)


# 自定义索引值


def ser_custom_index():
    hello1 = pd.Series([1, 3, 4, 5], index=['a', 'b', 'c', 'd'])

    print(hello1)


# 调用


def ser_invoke():
    print(hello1['a'])
    hello1['a'] = 100
    print(hello1['a'])


""" 
DataFrame
"""


# 声明
def df_declear():
    frame = pd.DataFrame(['a', 'b', 'c', 'd', 'e'], index=[
        1, 2, 3, 4, 5], columns=['hello'])

    print(frame)


# 从csv读取数据
def read_csv():
    frame = pd.read_csv("explames\\test.csv")

    print(frame)
    frame.to_csv("explames\\test_1.csv", index=False)
    json = frame.to_json()


# 从html读取
def read_html():
    html = request(
        'get', 'https://interactivebrokers.github.io/tws-api/message_codes.html#system_codes')

    print(html.text)

    table = SoupStrainer(name='table', attrs={'class': 'doxtable'})
    bs = BeautifulSoup(html.text, parse_only=table)
    msg_code_html = bs.prettify()

    frame_list = pd.read_html(msg_code_html)
    res = []
    new_columns = ['Code', 'TWS message', 'Additional notes']
    for i in frame_list:
        df = i.rename(columns=dict(zip(i.columns, new_columns)))
        res.append(df)

    frame = pd.concat(res)
    frame.to_csv("explames\\test_2.csv", index=False)


read_html()
