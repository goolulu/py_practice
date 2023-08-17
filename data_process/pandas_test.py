from typing import Hashable
from urllib import request
from uu import Error
import pandas as pd
from requests import request
from bs4 import BeautifulSoup, SoupStrainer
import numpy as np

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
    frame = pd.read_csv("explames\\test_1.csv",
                        encoding='gb2312')

    print(frame)
    frame.T.to_csv("explames\\test_2.csv", header=False)


# 从html读取
def read_html():
    html = ''
    try:
        with open('tags.txt', encoding='utf-8') as f:
            html = f.read()
    except IOError as e:
        print(e)
        print('失败')
        return
    bs = BeautifulSoup(html)
    msg_code_html = bs.prettify()

    frame_list = pd.read_html(msg_code_html)

    frame = pd.concat(frame_list)
    frame.to_csv('jj.csv', header=False)

# 层次化索引


def hindexing():
    data = pd.Series(np.arange(0, 4), index=[1, 2, 3, 4])

    multi_index = pd.MultiIndex.from_arrays(
        [[1, 1, 2, 2], ['a', 'b', 'c', 'd']])
    data2 = pd.Series(data=data.to_numpy(), index=multi_index)
    # print(multi_index)
    print(data)
    print(data2)


def sort_and_rearrangement():
    pass
