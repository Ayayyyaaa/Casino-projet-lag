import sqlite3

def creer_table():
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    #cursor.execute("""DROP TABLE IF EXISTS compte""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS compte (
        id_compte INTEGER PRIMARY KEY AUTOINCREMENT,
        pseudo TEXT UNIQUE NOT NULL,
        mdp TEXT,
        inventaire INTEGER DEFAULT 0)
        """)
    conn.close

creer_table()

def verifier_et_ajouter_pseudo(pseudo):
    """
    Vérifie si le pseudo existe déjà. Si non, il l'ajoute.
    """
    conn = sqlite3.connect("base_de_donnee2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM compte WHERE pseudo = ?", (pseudo,))
    compte = cursor.fetchone()
    if compte is None:
        # Ajouter le pseudo à la base
        cursor.execute("INSERT INTO compte (pseudo) VALUES (?)", (pseudo,))
        conn.commit()
        print(f"Le pseudo '{pseudo}' a été ajouté.")
        conn.close()
    else:
        print(f"Le pseudo '{pseudo}' existe déjà.")
        cursor.execute("SELECT (id_compte) FROM compte WHERE pseudo = ?", (pseudo,))
        id = cursor.fetchone()
        conn.close()
        return id

