import akshare as ak
import pandas as pd


def test():
    frame = ak.stock_szse_sector_summary(symbol='当月', date='202306')
    # for i in frame.itertuples():
    #     print(i)
    # print(frame)
    for i, row in frame.iterrows():
        print(row)


test()
