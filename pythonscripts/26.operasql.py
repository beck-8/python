import pymysql


sql_client = pymysql.connect(
    host='192.168.123.11',
    user='python',
    password='123456',
    cursorclass=pymysql.cursors.DictCursor
)

# try:
#     with sql_client.cursor() as cursors:
#         cursors.execute("create database if not exists pymysql_opera_db;")
#         cursors.execute("drop database if exists pymysql_test_db;")
#     sql_client.commit()
# except pymysql.MySQLError as error:
#     print(error)
# finally:
#     sql_client.close()   *6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9


try:
    with sql_client.cursor() as cursors:
        cursors.execute("select * from mysql.user;")
        result = cursors.fetchone()
        print(result)
        result = cursors.fetchone()
        print(result)
        result = cursors.fetchone()
        print(result)
        # result = cursors.fetchall()
        # print(result)
except pymysql.MySQLError as error:
    print(error)
finally:
    sql_client.close()
