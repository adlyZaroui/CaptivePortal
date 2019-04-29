import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "azerty",
                           db = "CaptivePortal")
    c = conn.cursor()

    return c, conn
