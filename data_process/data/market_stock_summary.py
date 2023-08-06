
from decimal import Decimal
import akshare
from datasource_manager import DBSession, engine
from trade_date_hist import TradeDate
from sqlalchemy import Column, String, DECIMAL, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd

Base = declarative_base()


class MarketStockSummary(Base):

    __tablename__ = 'market_stock_summary'

    __mapper_args__ = {
        'primary_key': ['assets_type', 'trade_date']
    }
    assets_type = Column(String(32))
    quantity = Column(DECIMAL())
    balance = Column(DECIMAL())
    total_market_value = Column(DECIMAL())
    liquid_market_value = Column(DECIMAL())
    trade_date = Column(String(8))

    def fetch_data(self, date):

        frame = akshare.stock_szse_summary(date)
        self.data = frame.fillna(value=0)
        self.write_data(date)

    def write_data(self, date):
        self.data['trade_date'] = date
        data = self.data.rename(columns=dict(zip(self.data.columns, [
                                'assets_type', 'quantity', 'balance', 'total_market_value', 'liquid_market_value', 'trade_date'])))
        data.to_sql(self.__tablename__, engine,
                    if_exists='append', index=False, method='multi')


def main():
    mss = MarketStockSummary()
    td = TradeDate()
    calendar_list = td.select_trade_date(
        first_date='20230801', end_date='20230805')
    for date in calendar_list:
        mss.fetch_data(date[0])


if __name__ == '__main__':
    main()
