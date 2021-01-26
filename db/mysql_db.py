import pymysql


class MySqlService:
    def __init__(self, host, user, password, db):
        self.connection = pymysql.connect(host=host,
                                          user=user,
                                          password=password,
                                          database=db,
                                          cursorclass=pymysql.cursors.DictCursor)

    def insert_query(self, query, data):
        with self.connection.cursor() as cursor:
            cursor.executemany(query, data)
        self.connection.commit()

    def get_query(self, query, single_field=False):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            if single_field:
                return [list(row.values())[0] for row in cursor.fetchall()]
            else:
                return cursor.fetchall()
