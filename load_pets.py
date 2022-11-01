import sqlite3

def load_pets(db):
    try:
        con = sqlite3.connect(db)
        with con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS Person")
            cur.execute("DROP TABLE IF EXISTS Pet")
            cur.execute("DROP TABLE IF EXISTS Person_Pet")
            cur.execute("CREATE TABLE Person(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)")
            cur.execute("CREATE TABLE Pet(id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER)")
            cur.execute("CREATE TABLE Person_Pet(person_id INTEGER, pet_id INTEGER)")
            cur.execute("INSERT INTO Person VALUES(1,'James','Smith', 41)")
            cur.execute("INSERT INTO Person VALUES(2,'Diana','Greene', 23)")
            cur.execute("INSERT INTO Person VALUES(3,'Sara','White', 27)")
            cur.execute("INSERT INTO Person VALUES(4,'William','Gibson', 23)")
            cur.execute("INSERT INTO Pet VALUES(1,'Rusty','Dalmation', 4, 1)")
            cur.execute("INSERT INTO Pet VALUES(2,'Bella','Alaskan Malamute', 3, 0)")
            cur.execute("INSERT INTO Pet VALUES(3,'Max', 'CockerSpaniel', 1, 0)")
            cur.execute("INSERT INTO Pet VALUES(4,'Rocky', 'Beagle', 7, 0)")
            cur.execute("INSERT INTO Pet VALUES(5,'Rufus', 'Cocker Spaniel', 1, 0)")
            cur.execute("INSERT INTO Pet VALUES(6,'Spot', 'Bloodhound', 2, 1)")
            cur.execute("INSERT INTO Person_Pet VALUES(1, 1)")
            cur.execute("INSERT INTO Person_Pet VALUES(1, 2)")
            cur.execute("INSERT INTO Person_Pet VALUES(2, 3)")
            cur.execute("INSERT INTO Person_Pet VALUES(2, 4)")
            cur.execute("INSERT INTO Person_Pet VALUES(3, 5)")
            cur.execute("INSERT INTO Person_Pet VALUES(4, 6)")
        con.commit()
        print("Inserted successfully!!")
    except Exception as e:
        print("error: ", e)
    finally:
        if con:
            con.close()

if __name__ == "__main__":
    db_name = 'pets.db'
    load_pets(db_name)
