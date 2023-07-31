import akshare as ak
import pandas as pd

from data.market_stock_summary import MarketStockSummary


def test():
<<<<<<< Updated upstream
    frame = ak.stock_szse_sector_summary(symbol='当月', date='202306')
    # for i in frame.itertuples():
    #     print(i)
    # print(frame)
    for i, row in frame.iterrows():
        print(row)
=======
    frame = ak.stock_szse_summary(date='20230728')

    mss = MarketStockSummary()

    mss.write_data(frame)
>>>>>>> Stashed changes


test()
