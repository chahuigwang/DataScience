import pymysql


def open_db():
    conn = pymysql.connect(host='localhost', user='root', password='cha990312', db='university')
    cur = conn.cursor(pymysql.cursors.DictCursor)

    return conn, cur


def close_db(conn, cur):
    cur.close()
    conn.close()