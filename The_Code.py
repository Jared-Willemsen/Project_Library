import mysql.connector

# Establish a connection to the database
conn = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="mydatabase"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute an SQL query
cursor.execute("SELECT * FROM mytable")

# Fetch the results of the query
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()