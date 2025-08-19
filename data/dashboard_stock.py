import streamlit as st
import os
import pandas as pd
from datetime import date

# Chemin vers les CSV transformés
DATA_PATH = "/home/kouki/iadev/distributech/data/transform"

# Dictionnaire des fichiers à charger
fichiers_csv = {
    "Régions": "regions_transforme.csv",
    "Revendeurs": "revendeurs_transforme.csv",
    "Produits": "produits_transforme.csv",
    "Productions": "productions_transforme.csv",
    "Paniers": "paniers_transforme.csv",
    "Commandes": "commandes_transforme.csv",
    "Commandes Produits": "commandes_produits_transforme.csv",
    "Stock" : "stock_disponible.csv"
}

# Configuration de la page Streamlit
st.set_page_config(page_title="Distributech - Dashboard", layout="wide")
st.title("Visualisation des Données Transformées")
st.caption(f"Date : {date.today().strftime('%d/%m/%Y')}")

# Sélecteur de table
choix_table = st.selectbox("Choisissez une table à explorer :", list(fichiers_csv.keys()))
fichier_selectionne = os.path.join(DATA_PATH, fichiers_csv[choix_table])

# Charger le CSV
if os.path.exists(fichier_selectionne):
    df = pd.read_csv(fichier_selectionne)
    st.subheader(f"Données : {choix_table}")
    st.dataframe(df, use_container_width=True)

    st.subheader("Graphe automatique")

    # Logique pour afficher un graphe pertinent par table
    colonnes = df.columns.str.lower()

    if "stock_disponible" in colonnes and "product_name" in colonnes:
        st.bar_chart(df.set_index("product_name")["stock_disponible"])

    elif "total_panier" in colonnes:
        st.bar_chart(df["total_panier"])

    elif "commande_date" in colonnes:
        df["commande_date"] = pd.to_datetime(df["commande_date"], errors="coerce")
        commandes_par_date = df.groupby("commande_date").size()
        st.line_chart(commandes_par_date)

    elif "produit_id" in colonnes and "quantite" in colonnes:
        st.bar_chart(df.groupby("produit_id")["quantite"].sum())

    else:
        st.info("Pas de graphe disponible pour ce tableau (colonnes non détectées).")

else:
    st.error(f"Fichier introuvable : {fichier_selectionne}")

