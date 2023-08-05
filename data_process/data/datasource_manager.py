import pymysql
import yaml
from sqlalchemy import Column, String, DECIMAL, create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'mysql+mysqlconnector://root:123456@47.107.60.105:3306/market', pool_size=20, max_overflow=10)
DBSession = sessionmaker(bind=engine)


class DataSourceManager():
    def __init__(self):
        f = open('data/config/application.yaml')
        config = yaml.full_load(f)
        self._user = config['datasource']['user']
        self._passwd = str(config['datasource']['passwd'])
        self._host = config['datasource']['host']
        self._port = config['datasource']['port']
        self._database = config['datasource']['database']

    def get_datasource(self):
        conn = pymysql.connect(host=self._host, port=self._port,
                               user=self._user, passwd=self._passwd,
                               database=self._database, charset='utf8mb4')
        return conn

    def write_data(self, data):
        pass

    def fetch_data(self):
        pass
