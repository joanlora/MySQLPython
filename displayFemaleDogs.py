import mysql.connector as mc # Joan Jose Lora

conn = mc.connect(host = 'localhost',user ='root', password = 'Idkbro', db = 'menagerie')
c = conn.cursor() 

c.execute("SELECT * FROM pet WHERE sex = 'f' AND species = 'dog';")
pd = c.fetchall()

for i in pd:
    print(i[0], i[1], i[2], i[3], i[4], i[5], i[6])