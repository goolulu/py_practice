import pymysql
from datasource_manager import DataSourceManager
import akshare as ak
import numpy as np
from datasource_manager import engine
import pandas as pd


class TradeDate(DataSourceManager):
    def __init__(self):
        super().__init__()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def write_data(self):
        conn = self.get_datasource()
        self.fetch_data()
        data = self._data.rename(dict(zip(self._data.columns, ['trade_date'])))
        data.to_sql(name='trade_date', con=conn,
                    if_exists='append', index=False, method='multi')

    def fetch_data(self):
        frame = ak.tool_trade_date_hist_sina()
        self._data = frame

    def select_trade_date(self, first_date, end_date):
        conn = self.get_datasource()
        select_sql = 'select * from trade_date where date between %(first_date)s and %(end_date)s'
        data = pd.read_sql(select_sql, con=conn, params={
            'first_date': first_date, 'end_date': end_date})
        return data.rename(columns=dict(zip(data.columns, ['trade_date'])))

    def select_month_date(self, first_date: str, end_date: str) -> []:
        data = self.select_trade_date(first_date, end_date)
        data['date_time'] = pd.to_datetime(data['trade_date'])
        data['year'] = data['date_time'].dt.year
        data['month'] = data['date_time'].dt.month
        group = data.groupby(['year', 'month'])
        res = []
        for (year, month), g in group:
            res.append('{}{:02d}'.format(year, month))

        return res


def main():
    td = TradeDate()

    d = td.select_month_date('201901', '20230731')
    print(d)


if __name__ == '__main__':
    main()
