from db_config import get_connection

class User:
    def __init__(self):
        self.__conn = get_connection()
        self.__cursor = self.__conn.cursor()

    def create_user(self, name):
        query = "INSERT INTO users (name) VALUES (%s)"
        self.__cursor.execute(query, (name,))
        self.__conn.commit()

    def get_users(self):
        self.__cursor.execute("SELECT * FROM users")
        return self.__cursor.fetchall()