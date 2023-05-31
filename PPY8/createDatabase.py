import sqlite3

db = sqlite3.connect("studenci.db")
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE "Ocena" (
	    "IdOcena"	INTEGER NOT NULL,
	    "IdStudent"	INTEGER NOT NULL,
	    "IdPrzedmiot"	INTEGER NOT NULL,
	    "Ocena"	TEXT NOT NULL,
	    CONSTRAINT "Ocena_pk" PRIMARY KEY("IdOcena" AUTOINCREMENT),
	    CONSTRAINT "Ocena_Student" FOREIGN KEY("IdStudent") REFERENCES "Student"("IdStudent"),
	    CONSTRAINT "Ocena_Przedmiot" FOREIGN KEY("IdPrzedmiot") REFERENCES "Przedmiot"("IdPrzedmiot")
)
    );
''')

cursor.execute('''
    CREATE TABLE "Przedmiot" (
	    "IdPrzedmiot"	INTEGER NOT NULL,
	    "Nazwa"	TEXT NOT NULL,
	    CONSTRAINT "Przedmiot_pk" PRIMARY KEY("IdPrzedmiot" AUTOINCREMENT)
)
''')
cursor.execute('''
    CREATE TABLE Student (
        CREATE TABLE "Student" (
	    "IdStudent"	INTEGER NOT NULL,
	    "Imie"	TEXT NOT NULL,
	    "Nazwisko"	TEXT NOT NULL,
	    CONSTRAINT "Student_pk" PRIMARY KEY("IdStudent" AUTOINCREMENT)
)
    );
''')
cursor.execute('''
    CREATE TABLE sqlite_sequence(name,seq)
''')
db.commit()
db.close()