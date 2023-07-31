from os import write
from datasource_manager import DataSourceManager
import pymysql
import akshare as ak


class StockSectorSummary(object):
    def __init__(self, data):
        self._data = data

    def write_data(self):
        conn = pymysql.connect(host='47.107.60.105', port=3306,
                               user='root', passwd='123456', database='market', charset='utf8mb4')
        try:
            with conn.cursor() as cursor:
                cursor.executemany('insert into ', self._data)
        except pymysql.MySQLError as error:
            conn.rollback()
            print(error)
        finally:
            conn.close()

    def get_data(self):
        frame = ak.stock_szse_sector_summary(symbol='当月', date='202306')
        self._data = frame


def main():
    sss = StockSectorSummary([])
    sss.get_data()
    sss.write_data()


if __name__ == '__main__':
    main()
