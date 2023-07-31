
import pymysql
import akshare

from datasource_manager import DataSourceManager


class MarketStockSummary(DataSourceManager):

    def __init__(self):
        DataSourceManager.__init__(self)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data
        pass

    def write_data(self):
        self.fetch_data()
        insert_sql = 'insert into market_stock_summary(assets_type, quantity, balance, total_market_value, liquid_market_value) values(%s, %f, %f, %f, %f)'
        conn = self.get_datasource()
        try:
            with conn.cursor() as cursor:
                rows = cursor.execute(insert_sql, self._data)
        except pymysql.MySQLError as error:
            conn.rollback()
            print(error)
        finally:
            conn.close()
        return rows

    def fetch_data(self):
        frame = akshare.stock_szse_summary()
        self._data = frame


def main():
    mss = MarketStockSummary()
    mss.write_data()


if __name__ == '__main__':
    main()
