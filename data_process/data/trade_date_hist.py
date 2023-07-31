import pymysql
from datasource_manager import DataSourceManager
import akshare as ak
import numpy as np


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
        insert_sql = 'insert into trade_date (date) values(%s)'
        conn = self.get_datasource()
        self.fetch_data()
        data_list = []
        for i in np.array(self._data).reshape(-1):
            data_list.append(i.strftime('%Y%m%d'))
        try:
            with conn.cursor() as cursor:
                cursor.executemany(insert_sql, data_list)
                conn.commit()
        except pymysql.MySQLError as error:
            print(error)
            conn.rollback()
        finally:
            conn.close()

    def fetch_data(self):
        frame = ak.tool_trade_date_hist_sina()
        self._data = frame


def main():
    td = TradeDate()
    td.write_data()


if __name__ == '__main__':
    main()
