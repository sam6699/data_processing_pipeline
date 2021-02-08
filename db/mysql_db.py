import pymysql


class MySqlService:
    def __init__(self, host, user, password, db):
        self._connection = pymysql.connect(host=host,
                                          user=user,
                                          password=password,
                                          database=db,
                                          cursorclass=pymysql.cursors.DictCursor)
    @property
    def connection(self):
        return self._connection
