import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="password", database="mydatabase"
)


def shard_data(data):
    shard_key = hash(data) % 4
    return shard_key


def insert_data(data):
    shard_key = shard_data(data)
    mycursor = mydb.cursor()
    sql = "INSERT INTO table{} (data) VALUES (%s)".format(shard_key)
    val = (data,)
    mycursor.execute(sql, val)
    mydb.commit()


def query_data(data):
    shard_key = shard_data(data)
    mycursor = mydb.cursor()
    sql = "SELECT * FROM table{} WHERE data = %s".format(shard_key)
    val = (data,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return result
