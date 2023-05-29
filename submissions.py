import os
import sqlite3

conn = sqlite3.connect("db.sqlite3")
cur = conn.cursor()

while True:
    submissions = os.listdir("submissions")
    if len(submissions) == 0:
        print("Everything is done :)")
        exit(0)

    first_submission = submissions[0]

    os.startfile(f".\\submissions\\{first_submission}")
    bottles = input("Enter the amount of bottles: ")
    query = f"UPDATE ecosite_accountmodel SET bottles = bottles" + f"+ {bottles} WHERE id=\"{first_submission.split('.')[0].replace('-', '')}\""
    print(query)
    cur.execute(query)
    conn.commit()
    os.remove(f".\\submissions\\{first_submission}")
