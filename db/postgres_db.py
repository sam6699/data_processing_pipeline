import psycopg2


class PostgresService:
    def __init__(self, host, port, username, password, db):
        self._connection = psycopg2.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=db,
        )
    
    @property
    def connection(self):
        return self._connection


class Singleton:

    __instance = None

    def __init__(self, host, port, username, password, db):
        self._connection = psycopg2.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=db)
            
    @classmethod
    def get_instance(self,host,port,username,password, db):
        if not self.__instannce:
            self.__instance = Singleton(host,port,username,password, db)
        return self.__instance


    @property
    def connection(self):
        return self._connection
