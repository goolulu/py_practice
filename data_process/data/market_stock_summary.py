
import pymysql
import akshare
from trade_date_hist import TradeDate

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

    def write_data(self, date):
        insert_sql = 'insert into market_stock_summary(assets_type, quantity, balance, total_market_value, liquid_market_value, trade_date) values(%s, %s, %s, %s, %s, %s)'

        conn = self.get_datasource()
        try:
            with conn.cursor() as cursor:
                self.data['date'] = date
                rows = cursor.executemany(
                    insert_sql, self.data.values.tolist())
                conn.commit()
        except pymysql.MySQLError as error:
            conn.rollback()
            print(error)
        finally:
            conn.close()

        return rows

    def fetch_data(self, date):
        frame = akshare.stock_szse_summary(date)
        self.data = frame.fillna(value=0)
        self.write_data(date)


def main():
    mss = MarketStockSummary()
    td = TradeDate()
    calendar_list = td.select_trade_date(
        first_date='20190101', end_date='20230731')
    for date in calendar_list:
        mss.fetch_data(date[0])


if __name__ == '__main__':
    main()
