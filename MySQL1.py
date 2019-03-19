# copy/pasted code from https://www.udemy.com/the-python-mega-course/learn/v4/t/lecture/12554126?start=0
# pip3 install mysql-connector

import mysql.connector
word = input("Enter a word in English and press Enter: ")
con = mysql.connector.connect(
    user="ardit700_student",
    password = "ardit700_student",
    host="108.167.140.122",
    database = "ardit700_pm1database"
)
cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()
if results:
    for result in results:
        print(result[1])
else:
    print("We couldn't find any results about that.")