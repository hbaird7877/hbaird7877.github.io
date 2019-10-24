
import csv

import psycopg2

import os

# Let's connect to our database
connection = psycopg2.connect(f"dbname=class_roster user={os.getlogin()}")

# Once a connection has been opened, we are going to open a cursor to run our SQL queries
cursor = connection.cursor()

# Let's create a query to create a students table and execute it. Note that we want to pass in values as %s rather than formatted strings to get away from SQL injection
student_table_creation_query = "CREATE TABLE students (id serial PRIMARY KEY, name varchar, favorite_food varchar);"
cursor.execute(student_table_creation_query)
cursor.execute("INSERT INTO students (name, favorite_food) VALUES (%s, %s)", ('Jon', "Sushi"))
cursor.execute("INSERT INTO students (name, favorite_food) VALUES (%s, %s)", ('Tom', "Mostaccioli"))
cursor.execute("INSERT INTO students (name, favorite_food) VALUES (%s, %s)", ('Mike', "Thai Curry"))

# This is how we'd query the database for the two students I created. Since nothing is going to get printed out, we've commented it out:
# cursor.execute("SELECT * FROM students;")

# Commit these changes to the database
connection.commit()

# Close communication with the database
cursor.close()
connection.close()