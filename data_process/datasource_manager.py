import pymysql


class DataSourceManager():
    def __init__(self, user, passwd, host, port, database):
        self._user = user
        self._passwd = passwd
        self._host = host
        self._port = port
        self._database = database

    def get_datasource(self):
        conn = pymysql.connect(host=self._host, port=self._port,
                               user=self._user, passwd=self._passwd,
                               database=self._database, charset='utf8mb4')
        return conn

    def write_data():
        pass


def main():
    s = DataSourceManager(user='root', passwd='123456',
                          host='47.107.60.105', port=3306, database='market')
    conn = s.get_datasource()
    print(conn)


if __name__ == '__main__':
    main()
