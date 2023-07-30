import akshare as ak
import pandas as pd


def test():
    frame = ak.stock_zh_a_hist(symbol='601318', period='daily',
                               start_date='20210531', end_date='20230731', adjust='qfq')
    print(frame)


test()
