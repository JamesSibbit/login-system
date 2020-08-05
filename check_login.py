import hashlib, getpass, pymysql

def connect(username, password, database = None):
    return pymysql.connect(host = 'localhost', user = username, passwd= password, db=database, autocommit = True)

#Get user login credentials
print("Please login to MySQL database")
print("")
user_name_sql = input("Please enter root username: ")
user_pass_sql = getpass.getpass(prompt="Please enter root password: ")

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
cursor.execute("USE user_pass")

def pass_check():
    for retry in range(5):
        username_check = input("Enter username: ")
        password_check = getpass.getpass('Enter password: ')
        hash_pass_check = hashlib.sha3_256()
        hash_pass_check.update(password_check.encode())
        cursor.execute("SELECT password FROM user_pass_table WHERE username = %s", username_check)
        sql_pass = cursor.fetchall()
        if hash_pass_check.hexdigest() == sql_pass[0][0]:
            print('Correct pass!')
            break
        print('Try Again')
    else:
        print('Too many tries')
        sys.exit(1)

pass_check()
