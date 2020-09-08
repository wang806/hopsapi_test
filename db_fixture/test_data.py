# import sys
# sys.path.append('../db_fixture')
# print(sys.path)
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

# create data

# Inster table datas
def init_data():
    datas = {
        'test':[
            {'name':'张一三'},
            {'name':'张二木'},
            {'name':'张三石'},
            {'name':'张四光'},
            {'name':'张五国'},
        ],
        'test_1':[
            {'name':'alen_li'},
            {'name':'has_jack'},
            {'name':'tom_tony'}
        ]
    }
    DB().init_data(datas)


if __name__ == '__main__':
    init_data()
