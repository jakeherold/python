#!/bin/python3
# A little bitty sqlite sandbox by a little bitty python programmer
# A mini-project for fun and no profit
# Created by Jake Herold
# If you're reading, utilizing, redistributing, or learning from this code you hearin agree to not judge my terrible code. 
# Teaching Source: https://www.youtube.com/watch?v=pd-0G0MigUA
# SQLite Data Types Source: https://www.sqlite.org/datatype3.html
# Version 0.0.1

# Modules and Resources
import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db') # If you want a fresh DB done for each run that purely lives in RAM, use ":memory: instead of 'employee.db"

c = conn.cursor()

# You only need to run this the first time you run the script. 
# c.execute("""CREATE TABLE employees (
#             first text,
#             last text,
#             pay interget
#             )""") # 3 quotes is a docstring. 


# Build Python Objects
emp_1 = Employee('Steve', 'asdf', 46789)
emp_2 = Employee('Ben', ';lkjlka;lsk', 32123)

# Inserts a data set into DB
# c.execute("INSERT INTO employees VALUES(?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay)) # Note: Don't use string formatting when pushing data into your table in python
# conn.commit()

# Alternate Method to Insert Data
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})
# conn.commit()


# Hardcoded SQL Query
c.execute("SELECT * FROM employees")
# print(c.fetchall())
data = c.fetchall()
for datum in data:
    print(str(datum) +'\n')

conn.commit()
conn.close()