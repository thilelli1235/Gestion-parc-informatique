import sqlite3
import os

db_name = "parc_informatique.db"

if os.path.exists(db_name):
    os.remove(db_name)
    print(f"❌ Ancien fichier '{db_name}' supprimé.")

conn = sqlite3.connect(db_name)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE equipement (
    type TEXT,
    marque TEXT,
    modele TEXT,
    serie TEXT PRIMARY KEY,
    localisation TEXT,
    etat TEXT
)
""")

donnees = [
    ("PC", "Dell", "OptiPlex 3080", "DEL001", "Bureau 101", "Opérationnel"),
    ("Portable", "HP", "EliteBook 840", "HP001", "Salle réunion", "Prêté"),
    ("Imprimante", "Canon", "PIXMA G6020", "CAN001", "Bureau 102", "Opérationnel"),
    ("Routeur", "Cisco", "RV340", "CIS001", "Salle serveurs", "Opérationnel"),
    ("Écran", "Samsung", "S24R350", "SAM001", "Bureau 103", "En panne"),
    ("PC", "Lenovo", "ThinkCentre M75", "LEN001", "Bureau 104", "Opérationnel"),
    ("Portable", "Apple", "MacBook Pro", "APP001", "Direction", "Opérationnel"),
    ("Imprimante", "Epson", "WorkForce Pro", "EPS001", "Bureau 105", "Hors service"),
    ("Routeur", "TP-Link", "Archer AX50", "TPL001", "Open Space", "Opérationnel"),
    ("Écran", "LG", "24MP400-B", "LG001", "Bureau 106", "Opérationnel")
]

for eq in donnees:
    cursor.execute("INSERT INTO equipement VALUES (?,?,?,?,?,?)", eq)


conn.commit()
conn.close()

print(f"✅ Fichier '{db_name}' créé avec {len(donnees)} équipements")
print("📍 Emplacement:", os.path.abspath(db_name))
input("\nAppuyez sur Entrée pour fermer...")