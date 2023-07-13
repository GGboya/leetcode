import mysql.connector
from decouple import config

def init():

    conn_mysql = mysql.connector.connect(
        host=config("HOST"),
        user=config("USER"),
        password=config("PASSWORD"),
        database=config("DATABASE"),
        auth_plugin="mysql_native_password"
    )
    return conn_mysql


def update(cursor, updated_level, title, qq,score, status):

    cursor.execute("UPDATE user SET level = %s, title = %s, score = %s, status = %s WHERE qq = %s", (updated_level, title, score, status, qq))

def insert(cursor, qq, score, status):
    cursor.execute("INSERT INTO user (qq, level, title, score, status) VALUES (%s, %s, %s,%s,%s)", (qq, 0, "普通成员", score, status))


def Retrieve(cursor, qq):
    cursor.execute("SELECT * FROM user WHERE qq = %s", (qq,))
    row = cursor.fetchone()
    return row
