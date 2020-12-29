import mysql.connector

my_db = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="19141918",
  database="employee_directory"
)

my_cursor = my_db.cursor()

# my_cursor.execute("SHOW DATABASES")
#
# for x in my_cursor:
#   print(x)

#my_db.database = "employee_directory"
my_cursor.execute("SHOW TABLES")

for x in my_cursor:
  print(x)

my_db.disconnect()
my_db.close()