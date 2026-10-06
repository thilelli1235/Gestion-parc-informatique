import sqlite3
import os

class Model:
    def __init__(self, db_name="parc_informatique.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._creer_table()
        self._verifier_et_remplir_donnees_test() # Vérifier si la table est vide et ajouter des données de test
    
    def _creer_table(self):
        """Crée la table si elle n'existe pas"""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipement (
            type TEXT NOT NULL,
            marque TEXT NOT NULL,
            modele TEXT NOT NULL,
            serie TEXT PRIMARY KEY,
            localisation TEXT NOT NULL,
            etat TEXT NOT NULL
        )
        """)
        self.conn.commit()
    
    def _verifier_et_remplir_donnees_test(self):
        """Vérifie si la table est vide et ajoute des données de test"""
        self.cursor.execute("SELECT COUNT(*) FROM equipement")
        count = self.cursor.fetchone()[0]
        
        if count == 0:
            print("Ajout de 10 équipements de test dans la base de données...")
            self._ajouter_donnees_test()
    
    def _ajouter_donnees_test(self):
        """Ajoute 10 équipements fictifs pour les tests"""
        donnees_test = [
            ("PC", "Dell", "OptiPlex 3080", "DEL-001", "Bureau 101", "Opérationnel"),
            ("Portable", "HP", "EliteBook 840", "HP-001", "Salle de réunion", "Prêté"),
            ("Imprimante", "Canon", "PIXMA G6020", "CAN-001", "Bureau 102", "Opérationnel"),
            ("Routeur", "Cisco", "RV340", "CIS-001", "Salle serveurs", "Opérationnel"),
            ("Écran", "Samsung", "S24R350", "SAM-001", "Bureau 103", "En panne"),
            ("PC", "Lenovo", "ThinkCentre M75", "LEN-001", "Bureau 104", "Opérationnel"),
            ("Portable", "Apple", "MacBook Pro", "APP-001", "Direction", "Opérationnel"),
            ("Imprimante", "Epson", "WorkForce Pro", "EPS-001", "Bureau 105", "Hors service"),
            ("Routeur", "TP-Link", "Archer AX50", "TPL-001", "Open Space", "Opérationnel"),
            ("Écran", "LG", "24MP400-B", "LG-001", "Bureau 106", "Opérationnel"),
            ("PC", "Asus", "ExpertCenter D5", "ASU-001", "Bureau 201", "Opérationnel"),
            ("Portable", "Acer", "Swift 3", "ACE-001", "Salle formation", "Prêté"),
            ("Serveur", "Dell", "PowerEdge T40", "DEL-002", "Salle serveurs", "Opérationnel"),
            ("Tablette", "Samsung", "Galaxy Tab S7", "SAM-002", "Accueil", "Opérationnel")
        ]
        
        for equipement in donnees_test:
            try:
                self.cursor.execute(
                    "INSERT INTO equipement VALUES (?, ?, ?, ?, ?, ?)",
                    equipement
                )
            except sqlite3.IntegrityError: # Ignorer les numéros de série en double
               pass
        
        self.conn.commit()
        print(f"{len(donnees_test)} équipements de test ajoutés avec succès.")
    
    def ajouter_equipement(self, equipement):
        """Ajoute un nouvel équipement"""
        try:
            self.cursor.execute(
                "INSERT INTO equipement VALUES (?, ?, ?, ?, ?, ?)",
                equipement
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def rechercher_equipement(self, critere, valeur):
        """Recherche des équipements selon un critère"""
        if not valeur.strip():
            return []
        
    
        mapping = {
            "type": "type",
            "localisation": "localisation",
            "etat": "etat",
            "serie": "serie"
        }
        
        critere_db = mapping.get(critere, "type")
        query = f"SELECT * FROM equipement WHERE {critere_db} LIKE ?"
        self.cursor.execute(query, (f"%{valeur}%",))
        return self.cursor.fetchall()
    
    def modifier_equipement(self, equipement):
        """Modifie un équipement existant"""
        try:
            self.cursor.execute("""
            UPDATE equipement 
            SET type=?, marque=?, modele=?, localisation=?, etat=?
            WHERE serie=?
            """, (
                equipement[0],  
                equipement[1],  
                equipement[2],  
                equipement[4],  
                equipement[5],  
                equipement[3]   
            ))
            self.conn.commit()
            return True
        except:
            return False
    
    def supprimer_equipement(self, serie):
        """Supprime un équipement"""
        self.cursor.execute("DELETE FROM equipement WHERE serie=?", (serie,))
        self.conn.commit()
    
    def afficher_tous(self):
        """Retourne tous les équipements triés par type et localisation"""
        self.cursor.execute("SELECT * FROM equipement ORDER BY type, localisation")
        return self.cursor.fetchall()
    
    def verifier_serie_existe(self, serie):
        """Vérifie si un numéro de série existe déjà"""
        self.cursor.execute("SELECT serie FROM equipement WHERE serie=?", (serie,))
        return self.cursor.fetchone() is not None
    
    def obtenir_statistiques(self):
        """Retourne des statistiques sur la base de données"""
        self.cursor.execute("SELECT COUNT(*) FROM equipement")
        total = self.cursor.fetchone()[0]
        
        self.cursor.execute("SELECT COUNT(DISTINCT type) FROM equipement")
        types = self.cursor.fetchone()[0]
        
        return {
            "total_equipements": total,
            "nombre_types": types
        }
    
    def exporter_sql(self, fichier_sql="export_parc.sql"):
        """Exporte la base de données en fichier SQL"""
        with open(fichier_sql, 'w', encoding='utf-8') as f:
            
            f.write("-- Export de la base de données du parc informatique\n")
            f.write("-- Généré automatiquement\n\n")
            
           
            f.write("-- Création de la table\n")
            f.write("CREATE TABLE IF NOT EXISTS equipement (\n")
            f.write("    type TEXT NOT NULL,\n")
            f.write("    marque TEXT NOT NULL,\n")
            f.write("    modele TEXT NOT NULL,\n")
            f.write("    serie TEXT PRIMARY KEY,\n")
            f.write("    localisation TEXT NOT NULL,\n")
            f.write("    etat TEXT NOT NULL\n")
            f.write(");\n\n")
            
            self.cursor.execute("SELECT * FROM equipement ORDER BY type, serie") # Récupérer toutes les données
            equipements = self.cursor.fetchall()
            
            if equipements:
                f.write("-- Insertion des équipements\n")
                for eq in equipements:
                    f.write(f"INSERT INTO equipement VALUES ('{eq[0]}', '{eq[1]}', '{eq[2]}', '{eq[3]}', '{eq[4]}', '{eq[5]}');\n")
            
           
            f.write(f"\n-- Statistiques\n")
            f.write(f"-- Total équipements: {len(equipements)}\n")
            
            self.cursor.execute("SELECT type, COUNT(*) FROM equipement GROUP BY type") # Compter par type
            types = self.cursor.fetchall()
            for type_eq, count in types:
                f.write(f"-- {type_eq}: {count} équipement(s)\n")
        
        print(f"Export SQL créé : {fichier_sql}")
        return fichier_sql
    
    def fermer(self):
        self.conn.close()