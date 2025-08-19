# Distributech
README — Mini-projet ETL Distributech🚀
               *********
               
📑 Table des matières

1) Description du projet
2) Fonctionnalités
3) Pré-requis
4) Technologies et langages utilisés
5) Guide d’installation
6) Guide de développement
7) Schéma d’architecture
8) Visuel du frontend
9) Licence
    
                 ____________________________________________________________________
   
📖 Description du projet


Ce projet consiste en la création d’un pipeline ETL (Extraction, Transformation, Chargement) pour Distributech, un grossiste en équipements électroniques.
L’objectif principal est de centraliser, transformer et charger les données provenant de différentes sources (SQLite, CSV) vers une base de données MySQL, afin de :

-Suivre les ventes et productions,
-Calculer le stock disponible en temps réel,
-Améliorer la prise de décision grâce à des données consolidées.

                 ____________________________________________________________________
                 
⚡ Fonctionnalités

1) Extraction depuis SQLite et fichiers CSV.
2) Transformation des données :
   
    -Nettoyage et suppression des doublons
   
    -Conversion des dates
   
    -Calcul du total_ligne par commande
   
    -Calcul du total_panier
   
    -Génération de la table produits_commandes
   
    -Suivi du stock (suivi_stock)
   

4) Chargement des données dans MySQL .
   
                 ____________________________________________________________________
   

🛠️ Pré-requis
Avant d’installer le projet, vous devez avoir :
    Python 3.10+
    MySQL 8+
    SQLite 3
    pip et virtualenv (optionnel mais recommandé)
    Fichier .env 
    
                 ____________________________________________________________________
                 
💻 Technologies et langages utilisés

    Python 3 (ETL)
    pandas → manipulation des données
    mysql.connector → connexion MySQL
    sqlite3 → connexion SQLite
    dotenv → gestion des variables d’environnement
    MySQL → base de données cible
    SQLite → base source (données initiales)
    Git / GitHub → gestion de version
    
                 _____________________________________________________________________
                 

🚀 Guide d’installation

Cloner le projet:
    git clone https://github.com/khaoulaMili123/distributech
    cd DISTRIBUTECH 
                
Créer un environnement virtuel et installer les dépendances:

    python -m venv venv
    source venv/bin/activate   # Linux / Mac
    venv\Scripts\activate      # Windows
    pip install -r requirements.txt

Créer la base MySQL:
    python bdd_creat.py

Lancer le pipeline ETL:
    python main.py

🛠️ Guide de développement

📂 Structure du projet :

etl_pipeline/

│
├── extraire_donnee/       # Scripts d'extraction

├── transformation/        # Scripts de transformation

│   └── transform_all

│   └── suivi_stock 

├── load/                  # Scripts de chargement 

├── bdd_creat/             # Création de base des données sur MySql

└── main.py                # Orchestrateur du pipeline ETL

=======

📜 Licence

Ce projet est sous licence MIT – vous êtes libre de l’utiliser, le modifier et le distribuer, sous réserve de conserver les crédits d’auteur.

=======

Créateurs du projets: 

[Khaoula MILI](https://github.com/khaoulaMili123)
[Hugo Babin](https://github.com/hugobabin)
[Corto Gayet](https://github.com/CortoGyt)
