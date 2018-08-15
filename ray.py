import sqlite3

conn = sqlite3.connect('test.db')

print ("Opened database successfully");

conn.execute('''CREATE TABLE IF NOT EXISTS INFORMATION
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50));''')
print ("Table created successfully");

conn.commit()

conn.execute("""INSERT INTO INFORMATION (ID,NAME,AGE,ADDRESS) VALUES ('1', 'Anupa', 24, 'Daarchula')""")

conn.execute("""INSERT INTO INFORMATION (ID,NAME,AGE,ADDRESS) VALUES ('2', 'Reshub', 22, 'Kathmandu')""")

conn.execute("""INSERT INTO INFORMATION (ID,NAME,AGE,ADDRESS) VALUES ('3', 'Shubham', 23, 'Mahendranagar')""")

conn.execute("""INSERT INTO INFORMATION (ID,NAME,AGE,ADDRESS) VALUES ('4', 'Swopnil', 22, 'Chitwan')""")

conn.commit()
print ("Records created successfully");
conn.commit()
#selection
#cursor = conn.execute("SELECT id, name, age, address  from INFORMATION")
#for row in cursor:
  # print ("ID = ", row[0])
  # print ("NAME = ", row[1])
  # print ("AGE = ", row[2])
   #print ("ADDRESS = ", row[3]), "\n"

#print ("Operation done successfully");
#conn.commit()
#updation
#conn.execute("UPDATE INFORMATION set AGE = 33 where ID = 1")
#conn.commit
#print ("Total number of rows updated :"), conn.total_changes
#cursor = conn.execute("SELECT id, name, age, address from INFORMATION")
#for row in cursor:
  # print ("ID = ", row[0])
  # print ("NAME = ", row[1])
  # print ("AGE = ", row[2])
  # print ("ADDRESS = ", row[3]), "\n"
#print ("Operation done successfully");
#conn.commit()
#deletion
#conn.execute("DELETE from INFORMATION where ID = 2;")
#conn.commit()
#print ("Total number of rows deleted :"), conn.total_changes
#cursor = conn.execute("SELECT id, name, age, address from INFORMATION")
#for row in cursor:
  # print ("ID = ", row[0])
  # print ("NAME = ", row[1])
   #print ("AGE = ", row[2])
   #print ("ADDRESS = ", row[3]), "\n"

#print ("Operation done successfully");
#conn.commit()
