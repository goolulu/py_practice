from os import write
from datasource_manager import DataSourceManager
import pymysql
import akshare as ak
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


class StockSectorSummary(DataSourceManager):
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def write_data(self, data):
        conn = self.get_datasource()
        try:
            with conn.cursor() as cursor:
                cursor.executemany('insert into ', self._data)
        except pymysql.MySQLError as error:
            conn.rollback()
            print(error)
        finally:
            conn.close()

    def get_data(self, symbol=None, date=None):
        frame = ak.stock_szse_sector_summary(symbol='当年', date='202306')
        print(frame)
        self.data = frame


def main():
    sss = StockSectorSummary([])
    sss.get_data()


if __name__ == '__main__':
    # d = ak.stock_zh_a_spot_em()
    # print(d)

    print(11669.91+107406.23)
