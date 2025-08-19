from extraire_donnee import extraire_donnees
from transformation.transform_all import transformer_donnees
from bdd_creat import create_db
from load import load_db
from transformation.suivi_stock import exporter_stock_disponible_csv

def main():
    print("\n===EXTRACTION===")
    donnees_brutes = extraire_donnees()

    print("\n===TRANSFORMATION===")
    transformer_donnees(donnees_brutes)

    print("\n===CRÉATION BASE DE DONNÉES===")
    create_db()

    print("\n===CHARGEMENT DES DONNÉES===")
    load_db()

    print("\n===EXPORT STOCK DISPONIBLE===")
    exporter_stock_disponible_csv()

if __name__ == "__main__":
    main()