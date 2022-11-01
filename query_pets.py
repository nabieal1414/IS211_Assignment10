import sqlite3

con = None

def db_connect(db):
    con = sqlite3.connect(db)
    return con

def get_pet_by_id(id):
    try:
        query = "SELECT * from Pet where id = ?"
        cur = con.cursor()
        cur.execute(query, (id,))
        record = cur.fetchone()
        return record
    except Exception as e:
        print("error:", e)


def get_person_by_id(id):
    try:
        query = "SELECT * from Person where id = ?"
        cur = con.cursor()
        cur.execute(query, (id,))
        person_record = cur.fetchone()
        if person_record != None:
            print(person_record[1],person_record[2], person_record[3],"years old")
            query = "SELECT * from Person_Pet where person_id = ?"
            cur.execute(query, (id,))
            person_pet_record = cur.fetchone()
            pet_id = person_pet_record[1]
            pet_record = get_pet_by_id(pet_id)
            print(person_record[1],person_record[2],"owned", pet_record[1]+",", "a",pet_record[2]+",", "that was",pet_record[3],"years old")
        else:
            print("Error: Person not found")
    except Exception as e:
        print("error:",e)
    finally:
        if con:
            con.close()

if __name__ == "__main__":
    db_name = "pets.db"
    while True:
        con = db_connect(db_name)
        person_id = int(input("Enter person id or press -1 to exit: "))
        if person_id == -1:
            break
        get_person_by_id(person_id)


