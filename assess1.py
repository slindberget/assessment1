import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="assessmentdb",
    user="postgres",
    password="Ghznmqm7"
    )

def read_contacts(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts;")
    rows = cur.fetchall()
    cur.close()
    return rows

def delete_contact(conn, first_name):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM contacts WHERE first_name = '{first_name}';")
    cur.close()

def add_contact(conn, first_name, last_name, title, organization):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO contacts(first_name, last_name, title, organization) VALUES ('{first_name}', '{last_name}', '{title}', '{organization}');")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    cmd = input("Hello and welcome to the contacts list, available commands: \nadd - add a contact\ndelete - delete a contact \nlist - list all contacts \nquit - quit the program\nsave -save withour quit\nhelp - help \nCommand: ").upper()
    if cmd == "LIST":
        print(read_contacts(conn))
    elif cmd == "ADD":
        first_name = input("  First name: ")
        last_name = input("  Last name: ")
        title = input("  title: ")
        organization = input("Organization:  ")
        add_contact(conn, first_name, last_name, title, organization)
    elif cmd == "DELETE":
        first_name = input("  Name: ")
        delete_contact(conn, first_name)
