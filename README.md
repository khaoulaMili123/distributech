# Distributech 🚀
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![MySQL](https://img.shields.io/badge/MySQL-8+-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![GitHub issues](https://img.shields.io/github/issues/khaoulaMili123/distributech)
![GitHub stars](https://img.shields.io/github/stars/khaoulaMili123/distributech?style=social)

---

📑 **Table des matières**

1. [Description du projet](#description-du-projet)
2. [Fonctionnalités](#fonctionnalités)
3. [Pré-requis](#pré-requis)
4. [Technologies et langages utilisés](#technologies-et-langages-utilisés)
5. [Guide d’installation](#guide-dinstallation)
6. [Guide de développement](#guide-de-développement)
7. [Schéma d’architecture](#schéma-darchitecture)
8. [Visuel du frontend](#visuel-du-frontend)
9. [Licence](#licence)
10. [Créateurs du projet](#créateurs-du-projet)

---

## 📖 Description du projet

Ce projet consiste en la création d’un **pipeline ETL** (Extraction, Transformation, Chargement) pour **Distributech**, un grossiste en équipements électroniques.  

**Objectifs principaux :**  
- 📊 Suivre les ventes et productions  
- 📦 Calculer le stock disponible en temps réel  
- 🤖 Améliorer la prise de décision grâce à des données consolidées  

---

## ⚡ Fonctionnalités

1. **Extraction** depuis SQLite et fichiers CSV  
2. **Transformation des données** :  
   - 🧹 Nettoyage et suppression des doublons  
   - 📅 Conversion des dates  
   - ➕ Calcul du total_ligne par commande  
   - 🛒 Calcul du total_panier  
   - 🗂️ Génération de la table `produits_commandes`  
   - 📈 Suivi du stock (`suivi_stock`)  
3. **Chargement** des données dans MySQL  

---

## 🛠️ Pré-requis

Avant d’installer le projet, vous devez avoir :  
- 🐍 Python 3.10+  
- 🐬 MySQL 8+  
- 🗄️ SQLite 3  
- 📦 pip et virtualenv (optionnel mais recommandé)  
- 🔑 Fichier `.env`  

---

## 💻 Technologies et langages utilisés

- 🐍 Python 3 (ETL)  
- 🐼 pandas → manipulation des données  
- 🔌 mysql.connector → connexion MySQL  
- 🗄️ sqlite3 → connexion SQLite  
- 🌿 dotenv → gestion des variables d’environnement  
- 🐬 MySQL → base de données cible  
- 🗄️ SQLite → base source  
- 📝 Git / GitHub → gestion de version  

---

## 🚀 Guide d’installation

**Cloner le projet :**

git clone https://github.com/khaoulaMili123/distributech
cd distributech

##Créer un environnement virtuel et installer les dépendances :

   -python -m venv venv
   
   -source venv/bin/activate   # Linux / Mac
   
   -venv\Scripts\activate      # Windows
   
   -pip install -r requirements.txt

##Créer la base MySQL :

   python bdd_creat.py


##Lancer le pipeline ETL :

   python main.py

🛠️ ##Guide de développement

##Structure du projet :
```
📂 distributech/

├── README.md

├── bdd/docker-compose.yml

├── data/

│   ├── base_stock.sqlite

│   ├── commande_revendeur_tech_express.csv

│   └── transform/        # Fichiers CSV transformés

├── requirements.txt

├── etl_pipeline/

│   ├── extraire_donnee/  # Scripts d'extraction

│   ├── transformation/   # Scripts de transformation

│   │   ├── transform_all

│   │   └── suivi_stock

│   └── load/             # Scripts de chargement

├── bdd_creat/            # Création de la base MySQL

└── main.py               # Orchestrateur du pipeline ETL
```

📜##Licence

Ce projet est sous licence MIT – vous êtes libre de l’utiliser, le modifier et le distribuer, sous réserve de conserver les crédits d’auteur.

👩‍💻 ##Créateurs du projet

- [Khaoula MILI](https://www.linkedin.com/in/hugo-babin-878451239/)
- 
- [Hugo BABIN](https://www.linkedin.com/in/khaoula-mili/)
- 
- [Corto GAYET](https://www.linkedin.com/in/corto-gayet-246aa32b3/)
- 


