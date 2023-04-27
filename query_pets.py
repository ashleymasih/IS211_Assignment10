import sqlite3
connection = sqlite3.connect('./pets.db')
c = connection.cursor()

while True:
    person_id = int(input("Enter ID (or -1 to quit): "))
    if person_id == -1:
        break
    
    c.execute("SELECT * FROM person WHERE id=?", (person_id,))
    person = c.fetchone()
    if not person:
        print("Person doesn't exist")
        continue
    
    print(f"{person[1]} {person[2]}, {person[3]} years old")
    
    c.execute("SELECT pet.name, pet.breed, pet.age, pet.dead FROM pet JOIN person_pet ON pet.id=person_pet.pet_id WHERE person_pet.person_id=?", (person_id,))
    pets = c.fetchall()
    if not pets:
        print(f"{person[1]} {person[2]} doesn't have any pets")
    else:
        for pet in pets:
            status = "dead" if pet[3] else "alive"
            print(f"{person[1]} {person[2]} owned {pet[0]}, a {pet[1]}, that was {pet[2]} years old and {status}")
    
# Close the database connection
connection.close()