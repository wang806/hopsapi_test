import configparser as cparser
import pymysql.cursors
import os

base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + '/config.ini'
cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get('mysqlconf', 'host')
port = cf.get('mysqlconf', 'port')
db = cf.get('mysqlconf', 'db_name')
user = cf.get('mysqlconf', 'user')
password = cf.get('mysqlconf', 'password')


class DB:

    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host, port=int(port), user=user,
                                              password=password, db=db, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def query(self, _sql):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(_sql)
                _data = cursor.fetchall()
                # 提交到数据库执行
                cursor.execute(_sql)
                self.connection.commit()
                print(_data)
            except pymysql.Error:
                # 如果发生错误则回滚
                self.connection.rollback()
                return False
            return _data

    def clear(self, _table_name):
        real_sql = 'truncate ' + _table_name + ';'
        with self.connection.cursor() as cursor:
            cursor.execute('SET FOREIGN_KEY_CHECKS=0;')
            cursor.execute(real_sql)
        self.connection.commit()

    def inserts(self, _table_name, _table_data):
        for key in _table_data:
            _table_data[key] = "'" + str(_table_data[key]) + "'"
        key = ",".join(_table_data.keys())
        value = ",".join(_table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    def insert(self, _table_name, _table_data):
        real_sql = "INSERT INTO " + _table_name + " VALUES " + "(" + _table_data + ");"
        print(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    def close(self):
        self.connection.close()

    def init_data(self, _datas):
        for table, _data in _datas.items():
            self.clear(table)
            for d in _data:
                self.inserts(table, d)
        self.close()


if __name__ == '__main__':

    db = DB()
    table_name = "card_copy1"
    data = "NULL, 218, '朝阳合生汇粮食券', '朝阳合生汇粮食券,仅限餐饮类使用.', 45000, 50000, -9999, 1, 90.00, 0, 0, 1, 5, NULL, '2020-06-29 13:45:58', '2020-07-31 00:00:00', 0, '2020-06-29 11:49:02', '2038-01-01 00:00:00', 1, 1, 1, 1, 6889, '荆晓晨', '2020-06-29 11:49:02', '2020-06-30 13:57:42', 0, 00"

    # db.clear(table_name)
    # db.insert(table_name, data)
    # db.query('select * from card_copy1 where id=1;')
    result = db.query('select * from card;')
    for dt in result:
        print(dt)
    # db.query("delete from card where name = '121';")
    # db.close()
