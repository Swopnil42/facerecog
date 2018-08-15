def datarec(Id,name,address):
    import sqlite3
    import time
    import datetime
    import random
    conn = sqlite3.connect('facerecog.db')
    c = conn.cursor()

    def create_table():
        c.execute("CREATE TABLE IF NOT EXISTS facerecognize (Id INTEGER primary key, name TEXT, address TEXT)")
        
    def dynamic_data_entry(Id,name,add):
       
        stm = "INSERT INTO facerecognize VALUES ('{}','{}','{}')".format(Id, name, address)
        
        c.execute(stm)
        #c.execute("UPDATE facerecognize SET name=? WHERE Id=?",name)
        #c.execute("UPDATE facerecognize SET address=? WHERE Id=?",address)

       


    
    create_table()
    dynamic_data_entry(Id,name,address)
    c.close()
    conn.close()


datarec(0,'alvin','my house')
