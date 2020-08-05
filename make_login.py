import hashlib, pymysql
from getpass import getpass

def connect(username, password, database = None):
    return pymysql.connect(host = 'localhost', user = username, passwd= password, db=database, autocommit = True)

#Get user login credentials
print("Please login to MySQL database")
print("")
user_name_sql = input("Please enter root username: ")
user_pass_sql = getpass(prompt="Please enter root password: ")

#Connect to SQL to create User
while True:
    try:
        con = connect(user_name_sql, user_pass_sql)
    except:
        print("Credentials not recognised, try again")
        user_name_sql = input("Please enter root username: ")
        user_pass_sql = getpass(prompt="Please enter root password: ")
        continue
    break

cursor = con.cursor()

def hashpassword(password):
    hash_pass = hashlib.sha3_256()
    hash_pass.update(password.encode())
    return hash_pass.hexdigest()

cursor.execute("CREATE DATABASE IF NOT EXISTS user_pass")
cursor.execute("USE user_pass")
cursor.execute("CREATE TABLE IF NOT EXISTS user_pass_table (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, username TEXT, password TEXT)")

print("")
user_name = input("Please choose a username: ")
user_pass = hashpassword(getpass("Please choose a password: "))

cursor.execute("INSERT INTO user_pass_table (username, password) VALUES (%s, %s)", (user_name, user_pass))

cursor.close()
