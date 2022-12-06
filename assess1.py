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