from database.connect import my_db

my_db.reconnect()

my_cursor = my_db.cursor()

my_cursor.execute("SELECT * FROM employee")

employees = my_cursor.fetchall()

print(employees)

my_cursor.execute("SELECT * FROM employee WHERE id = 1")

employee = my_cursor.fetchone()
print(employee)#tuple


