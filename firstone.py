import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "kutty",
    database = "testdb",
)
my_cursor = my_db.cursor()
#Creating database #
# my_cursor.execute("CREATE DATABASE testdb")
# my_cursor.execute("SHOW DATABASES")
# for i in my_cursor:
#     print (i[0])

#Create Table
# my_cursor.execute("CREATE TABLE user (name VARCHAR(50), email VARCHAR (100), age INTEGER (3), user_id INTEGER AUTO_INCREMENT primary key)")
# my_cursor.execute("SHOW TABLES")
# for i in my_cursor:
#     print (i[0])

#Insert sigle row into TABLE
# my_cursor.execute("INSERT INTO user (name, email, age) VALUES ('Jagadeesh', 'jagadeesh232419@gmail.com', 42)")
# sqlstuff = "INSERT INTO user (name, email, age) VALUES (%s, %s, %s)"
# rcd = ('chitti', 'chitt@gmail.com', 3)
# my_cursor.execute(sqlstuff,rcd)
# my_db.commit()

#Inser multiple row
# sqlstuff = "insert into user (name, email, age) VALUES (%s, %s, %s)"
# rcds = [
#     ('jyothi', 'jyothi@mail.com', 36),
#     ('ammu', 'ammu@mail.com', 13)
# ]
# my_cursor.executemany(sqlstuff,rcds)
# my_db.commit()

#Select from table and format the data
# my_cursor.execute("SELECT * FROM user")
# result = my_cursor.fetchall()
# print ('name\t\temail\t\t\tage\tuser_id')
# for row in result:
#     # print (row[0] + "\t" + row [1] + "\t" +  str(row [2]) + "\t" + str (row [3]) )
#     print (row[0] + "\t%s" %row[1] + "\t\t%s" %row[2] + "\t\t%s" %row[3])

#select form tbale using where clause
# my_cursor.execute("SELECT * FROM user WHERE age > 30")
# result = my_cursor.fetchall()
# print (result)

#Select from table using where clause wild characters
# my_cursor.execute("SELECT * from user where email like 'jagadeesh232419@_____.com'")
# result = my_cursor.fetchall()
# print (result)

#Update TABLE
# my_cursor.execute("SELECT * FROM user WHERE user_id = 3")
# result = my_cursor.fetchall()
# print (result)
# my_cursor.execute("UPDATE user SET age = 40 WHERE user_id = 3")
# my_db.commit()
# my_cursor.execute("SELECT * FROM user WHERE user_id = 3")
# result = my_cursor.fetchall()
# print (result)

#lIMIT result
# my_cursor.execute("SELECT * FROM user LIMIT 3 OFFSET 1")
# result = my_cursor.fetchall()
# print (result)

#Order by
# my_cursor.execute("SELECT * FROM user ORDER BY user_id DESC")
# result = my_cursor.fetchall()
# print (result

#Delete from TABLE
# sqlstuff = ("DELETE FROM user WHERE user_id = '7'")
# my_cursor.execute(sqlstuff)
# my_db.commit()

#Drop TABLE
my_sql = ("DROP TABLE IF EXISTS user")
my_cursor.execute(my_sql)
