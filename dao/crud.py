import mysql.connector
from decouple import config

def init():

    conn_mysql = mysql.connector.connect(
        host=config("HOST"),
        user=config("USER"),
        password=config("PASSWORD"),
        database=config("DATABASE")
    )
    return conn_mysql


def update(cursor, updated_level, title, qq):
    cursor.execute("UPDATE user SET level = %s, title = %s WHERE qq = %s", (updated_level, title, qq))


def insert(cursor, qq):
    cursor.execute("INSERT INTO user (qq, level, title) VALUES (%s, %s, %s)", (qq, 0, "普通成员"))


def Retrieve(cursor, qq):
    cursor.execute("SELECT * FROM user WHERE qq = %s", (qq,))
    row = cursor.fetchone()
    return row
