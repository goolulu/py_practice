from os import write
from turtle import left
from trade_date_hist import TradeDate
from datasource_manager import engine
import pymysql
import akshare as ak
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


class StockSectorSummary():

    __table_name__ = 'stock_sector_summary'

    __table_columns__ = [
        'name',
        'en_name',
        'trade_days',
        'trade_amount',
        'total_amount_ratio',
        'trade_quantity',
        'total_quantity_ratio',
        'trade_valume',
        'total_valume_ratio',
        'year_month',
        'type'
    ]

    def __init__(self, data):
        self._data = data

    def write_data(self, data: pd.DataFrame):
        data.to_sql(self.__table_name__, engine,
                    if_exists='append', index=False, method='multi')

    def get_data(self, symbol, date) -> pd.DataFrame:
        frame = ak.stock_szse_sector_summary(symbol=symbol, date=date)
        frame.reset_index()
        frame['year_month'] = date
        frame['type'] = symbol
        data = frame.rename(
            dict(zip(frame.columns, self.__table_columns__)), axis=1, errors='raise')
        return data


def main():
    sss = StockSectorSummary([])
    td = TradeDate()
    month_list = td.select_month_date('20190101', '20230806')

    for month in month_list:
        data = sss.get_data('当月', month)
        sss.write_data(data=data)


if __name__ == '__main__':
    data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                                  'pastrami', 'corned beef', 'bacon',
                                  'pastrami', 'honey ham', 'nova lox'],
                         'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

    print(data)

    meat_to_animal = pd.DataFrame.from_dict({
        'bacon': 'pig',
        'pulled pork': 'pig',
        'pastrami': 'cow',
        'corned beef': 'cow',
        'honey ham': 'pig',
        'nova lox': 'salmon'
    }, orient='index')

    data['animal'] = data['food'].map({
        'bacon': 'pig',
        'pulled pork': 'pig',
        'pastrami': 'cow',
        'corned beef': 'cow',
        'honey ham': 'pig',
        'nova lox': 'salmon'
    })
    print(data)
    # print(data.join(meat_to_animal, how=left))
