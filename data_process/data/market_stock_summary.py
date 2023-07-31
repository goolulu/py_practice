
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
        insert_sql = 'insert into market_stock_summary(assets_type, quantity, balance, total_market_value, liquid_market_value) values(%s, %s, %s, %s, %s)'

        conn = self.get_datasource()
        try:
            with conn.cursor() as cursor:
                data_list = self.data.values.tolist()
                rows = cursor.executemany(insert_sql, data_list)
                conn.commit()
        except pymysql.MySQLError as error:
            conn.rollback()
            print(error)
        finally:
            conn.close()

        return rows

    def fetch_data(self):
        frame = akshare.stock_szse_summary(date='20230731')
        self.data = frame.fillna(value=0)


def main():
    mss = MarketStockSummary()
    mss.write_data()


if __name__ == '__main__':
    main()
