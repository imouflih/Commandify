CREATE TABLE Client (
    N_client INTEGER PRIMARY KEY,
    Nom_client TEXT,
    Add_Postale TEXT,
    Add_email TEXT,
    Tel INTEGER,
    Facebook TEXT,
    Instagram TEXT
, fidelite integer);
CREATE TABLE Commande (
    N_Commande INTEGER PRIMARY KEY,
    N_client INTEGER,
    Date_commande DATE,
    FOREIGN KEY (N_client) REFERENCES Client(N_client)
);
CREATE TABLE Livraison (
    N_livraison INTEGER PRIMARY KEY,
    N_Commande INTEGER,
    Mode TEXT,
    Frais_livraison REAL,
    Date_livraison DATE,
    FOREIGN KEY (N_Commande) REFERENCES Commande(N_Commande)
);
CREATE TABLE Product (
    N_Product INTEGER PRIMARY KEY,
    prix_unitaire REAL
, name VARCHAR, prix_magazin real, statut VARCHAR);
CREATE TABLE Facture (
    N_facture INTEGER PRIMARY KEY,
    N_Commande INTEGER,
    Date_facture DATE,
    Prix_commande REAL,
    Frais_service REAL,
    Frais_livraison REAL,
    Montant_facture REAL,
    FOREIGN KEY (N_Commande) REFERENCES Commande(N_Commande)
);
CREATE TABLE Stock (
    N_Stock INTEGER PRIMARY KEY,
    N_Product INTEGER,
    Status TEXT,
    FOREIGN KEY (N_Product) REFERENCES Product(N_Product)
);
CREATE TRIGGER check_product_statut_insert
BEFORE INSERT ON product
FOR EACH ROW
BEGIN
    SELECT
    CASE
        WHEN NEW.statut NOT IN ('en stock', 'en rupture') THEN
            RAISE(ABORT, 'Invalid statut value')
    END;
END;
CREATE TRIGGER check_product_statut_update
BEFORE UPDATE ON product
FOR EACH ROW
BEGIN
    SELECT
    CASE
        WHEN NEW.statut NOT IN ('en stock', 'en rupture') THEN
            RAISE(ABORT, 'Invalid statut value')
    END;
END;