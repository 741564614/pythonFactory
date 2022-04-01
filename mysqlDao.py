import mysql.connector
from mysql.connector import IntegrityError


def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="exhunter"
    )
    return conn


def execute_sql(cursor, sql):
    try:
        cursor.execute(sql)
    except IntegrityError:
        print('重复的id')
