import sqlite3
con = sqlite3.connect('phonebook.db')
c = con.cursor()
#c.execute("CREATE TABLE Directory(ID text, name text, phone text, email text)")
data = [
    ('100','she','1234567890','she21ec@cmrit.ac.in'),
    ('101','he','1234567890','he21ec@cmrit.ac.in'),
    ('102','her','1234567890','her21ec@cmrit.ac.in'),
    ('103','him','1234567890','him21ec@cmrit.ac.in'),
    ('104','his','1234567890','his21ec@cmrit.ac.in'),
]
#c.executemany("INSERT INTO Directory (ID,name,phone,email) VALUES(?,?,?,?)",data)
c.execute("SELECT * FROM Directory")
for i in range(0,5):
    print(c.fetchone())
con.commit()
con.close()