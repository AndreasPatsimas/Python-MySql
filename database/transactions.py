from database.connect import my_db

my_db.reconnect()

my_cursor = my_db.cursor()

sql = "INSERT INTO employee (name, email) VALUES (%s, %s)"
val = ("Sot", "sot@luv2code.com")

my_cursor.execute(sql, val)

my_db.commit()

print(my_cursor.rowcount, "record(s) affected")