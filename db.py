import sqlite3

import config

connection = sqlite3.connect(config.BOT_DB_FILENAME, check_same_thread=False)
cursor = connection.cursor()


class Users:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Users, cls).__new__(cls)
        return cls.instance

    class __User:
        def __init__(self, user_id, user_name, interface_state):
            self.user_id = user_id
            self.user_name = user_name
            self.interface_state = interface_state

    @staticmethod
    def add(user_id, user_name):
        cursor.execute("INSERT INTO "
                       "users (user_id, user_name) "
                       "VALUES (?, ?)", (user_id, user_name)
                       )
        connection.commit()

    @staticmethod
    def exists(user_id):
        cursor.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,))
        return len(cursor.fetchall()) > 0

    def get(self, user_id):
        cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        user = cursor.fetchone()
        return self.__User(user[0], user[1], user[2])

    def __iter__(self):
        cursor.execute("SELECT user_id FROM users")
        for user in cursor.fetchall():
            yield self.get(user[0])

    @staticmethod
    def update_interface_state(user_id, interface_state):
        cursor.execute("UPDATE users SET interface_state=? WHERE user_id=?", (interface_state, user_id))
        connection.commit()


def create_tables():
    cursor.execute("CREATE TABLE IF NOT EXISTS "
                   "users ("
                   "user_id             INTEGER,"
                   "user_name           TEXT,"
                   "interface_state     INTEGER DEFAULT 0)")
    connection.commit()


create_tables()


def main():
    pass


if __name__ == '__main__':
    main()
