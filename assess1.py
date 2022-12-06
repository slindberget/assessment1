import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="assessmentdb",
    user="postgres",
    password="Ghznmqm7"
    )

def read_contacts(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM contacts;")
    rows = cur.fetchall()
    cur.close()
    return rows

while True: ## REPL - Read Execute Program Loop
    cmd = input("Hello and welcome to the contacts list, available commands: \nadd - add a phone number\ndelete - delete a contact \nlist - list all phone numbers \nquit - quit the program\nsave -save withour quit\nhelp - help \nCommand: ").upper()

