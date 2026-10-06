-- Export de la base de données du parc informatique
-- Généré automatiquement

-- Création de la table
CREATE TABLE IF NOT EXISTS equipement (
    type TEXT NOT NULL,
    marque TEXT NOT NULL,
    modele TEXT NOT NULL,
    serie TEXT PRIMARY KEY,
    localisation TEXT NOT NULL,
    etat TEXT NOT NULL
);

-- Insertion des équipements
INSERT INTO equipement VALUES ('Imprimante', 'Canon', 'PIXMA G6020', 'CAN-001', 'Bureau 102', 'Opérationnel');
INSERT INTO equipement VALUES ('Imprimante', 'Epson', 'WorkForce Pro', 'EPS-001', 'Bureau 105', 'Hors service');
INSERT INTO equipement VALUES ('Imprimante', 'Epson', 'WorkForce Pro', 'EPS-002', 'Bureau 105', 'Hors service');
INSERT INTO equipement VALUES ('PC', 'Asus', 'ExpertCenter D5', 'ASU-001', 'Bureau 206', 'Opérationnel');
INSERT INTO equipement VALUES ('PC', 'Dell', 'OptiPlex 3080', 'DEL-001', 'Bureau 102', 'Opérationnel');
INSERT INTO equipement VALUES ('PC', 'Dell', 'OptiPlex 3080', 'DEL-003', 'Bureau 102', 'Opérationnel');
INSERT INTO equipement VALUES ('PC', 'Lenovo', 'ThinkCentre M75', 'LEN-001', 'Bureau 104', 'Opérationnel');
INSERT INTO equipement VALUES ('Portable', 'iphone', '15', '001', 'maison', 'Prêté');
INSERT INTO equipement VALUES ('Portable', 'Acer', 'Swift 3', 'ACE-001', 'Salle formation', 'Prêté');
INSERT INTO equipement VALUES ('Portable', 'Apple', 'MacBook Pro', 'APP-001', 'Direction', 'Opérationnel');
INSERT INTO equipement VALUES ('Portable', 'HP', 'EliteBook 840', 'HP-001', 'Salle de réunion', 'Prêté');
INSERT INTO equipement VALUES ('Routeur', 'Cisco', 'RV340', 'CIS-001', 'Salle serveurs', 'Opérationnel');
INSERT INTO equipement VALUES ('Routeur', 'TP-Link', 'Archer AX50', 'TPL-001', 'Open Space', 'Opérationnel');
INSERT INTO equipement VALUES ('Serveur', 'Dell', 'PowerEdge T40', 'DEL-002', 'Salle serveurs', 'Opérationnel');
INSERT INTO equipement VALUES ('Tablette', 'Samsung', 'Galaxy Tab S7', 'SAM-002', 'Accueil', 'Opérationnel');
INSERT INTO equipement VALUES ('Écran', 'LG', '24MP400-B', 'LG-001', 'Bureau 106', 'Opérationnel');
INSERT INTO equipement VALUES ('Écran', 'Samsung', 'S24R350', 'SAM-001', 'Bureau 103', 'En panne');

-- Statistiques
-- Total équipements: 17
-- Imprimante: 3 équipement(s)
-- PC: 4 équipement(s)
-- Portable: 4 équipement(s)
-- Routeur: 2 équipement(s)
-- Serveur: 1 équipement(s)
-- Tablette: 1 équipement(s)
-- Écran: 2 équipement(s)
