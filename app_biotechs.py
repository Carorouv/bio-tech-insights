import streamlit as st
from PIL import Image


# Mise en place du background de l'application
def set_bg_hack_url():
    image_url = "https://raw.githubusercontent.com/Carorouv/bio-tech-insights/main/medical_wallpaper_2.jpg"
    st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("{image_url}") no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    




set_bg_hack_url()
# Logo centré en haut à gauche
logo ='https://raw.githubusercontent.com/Carorouv/bio-tech-insights/main/logobiotechinsight.png'
st.sidebar.image(Image.open('logobiotechinsight.png'), width=200, use_column_width=False)
# Définir une fonction pour le contenu de chaque page
def maladies_cardiaques():
    st.write('### Maladies cardiaques : renseignez les biomarqueurs de votre patient(e) et lancez le traitement.')
    # 5 champs pour la saisie des données
    data1 = st.text_input("Donnée 1")
    data2 = st.text_input("Donnée 2")
    data3 = st.text_input("Donnée 3")
    data4 = st.text_input("Donnée 4")
    data5 = st.text_input("Donnée 5")
    # Bouton pour lancer le traitement des données
    if st.button("Lancer le traitement"):
        # Ajoutez ici le code pour traiter les données des maladies cardiaques
        st.write("Traitement en cours...")
def maladies_du_foie():
    # Ajoutez le code pour la page "Maladies du foie" ici
    st.write('### Maladies du foie : renseignez les biomarqueurs de votre patient(e) et lancez le traitement.')
    # 5 champs pour la saisie des données
    data1 = st.text_input("Donnée 1")
    data2 = st.text_input("Donnée 2")
    data3 = st.text_input("Donnée 3")
    data4 = st.text_input("Donnée 4")
    data5 = st.text_input("Donnée 5")
    # Bouton pour lancer le traitement des données
    if st.button("Lancer le traitement"):
        # Ajoutez ici le code pour traiter les données des maladies du foie
        st.write("Traitement en cours...")
def maladie_renale_chronique():
    # Ajoutez le code pour la page "Maladie rénale chronique" ici
    st.write('### Maladie rénale chronique : renseignez les biomarqueurs de votre patient(e) et lancez le traitement.')
    # 5 champs pour la saisie des données
    data1 = st.text_input("Donnée 1")
    data2 = st.text_input("Donnée 2")
    data3 = st.text_input("Donnée 3")
    data4 = st.text_input("Donnée 4")
    data5 = st.text_input("Donnée 5")
    # Bouton pour lancer le traitement des données
    if st.button("Lancer le traitement"):
        # Ajoutez ici le code pour traiter les données de la maladie rénale chronique
        st.write("Traitement en cours...")
def diabete():
    # Ajoutez le code pour la page "Diabète" ici
    st.write('### Diabète : renseignez les biomarqueurs de votre patient(e) et lancez le traitement.')
    # 5 champs pour la saisie des données
    data1 = st.text_input("Donnée 1")
    data2 = st.text_input("Donnée 2")
    data3 = st.text_input("Donnée 3")
    data4 = st.text_input("Donnée 4")
    data5 = st.text_input("Donnée 5")
    # Bouton pour lancer le traitement des données
    if st.button("Lancer le traitement"):
        # Ajoutez ici le code pour traiter les données du diabète
        st.write("Traitement en cours...")
def cancer_du_sein():
    # Définition d'une fonction pour la page "Cancer du sein"
    st.write('### Cancer du sein : renseignez les biomarqueurs de votre patient(e) et lancez le traitement')
    # Champs pour la saisie des données
    mean_radius = st.number_input("Rayon moyen de la cellule", value=0.0000, step=0.0001, format="%.4f")
    mean_texture = st.number_input("Texture moyenne de la cellule", value=0.0000, step=0.0001, format="%.4f")
    mean_smoothness = st.number_input("Régularité moyenne de la cellule", value=0.0000, step=0.0001, format="%.4f")
    mean_compactness = st.number_input("Compacité moyenne de la cellule", value=0.0000, step=0.0001, format="%.4f")
    mean_concavity = st.number_input("Concavité moyenne de la cellule", value=0.0000, step=0.0001, format="%.4f")
    mean_concave_points = st.number_input("Point concave moyen de la cellule", value=0.0000, step=0.0001, format="%.4f")
    mean_symmetry = st.number_input("Symétrie moyenne de la cellule", value=0.0000, step=0.0001, format="%.4f")
    mean_fractal_dimension = st.number_input("Dimension fractale moyenne de la cellule", value=0.0000, step=0.0001, format="%.4f")
    # Bouton pour Diagnostic des données
    if st.button("Diagnostic"):
        # Vérification si toutes les entrées sont nulles
        if all(value == 0 for value in [mean_radius, mean_texture, mean_smoothness, mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension]):
            st.warning("Veuillez renseigner les biomarqueurs de vos patients pour pouvoir faire une prédiction.")
        else:
            # Création du tableau NumPy avec les données saisies par l'utilisateur
            my_data = np.array([[mean_radius, mean_texture, mean_smoothness, mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension]])
            # Chargement du scaler PowerTransformer
            scaler = PowerTransformer()
            # Ajustement du scaler aux données d'entraînement
            scaler.fit(my_data)
            # Normalisation des données avec le scaler PowerTransformer
            my_data_scaled = scaler.transform(my_data)
            # Prédictions avec le modèle de cancer du sein CatBoost entraîné
            predictions = model_cancer_breast.predict(my_data_scaled)
            # Affichage du résultat de la prédiction
            if predictions[0] == 0:
                st.write("Le modèle prédit que le patient n'a pas de cancer du sein.")
            else:
                st.write("Le modèle prédit que le patient a un risque de développer un cancer du sein.")


    # Ajoutez le code pour la page "Cancer du sein" ici
    st.write('### Cancer du sein : renseignez les biomarqueurs de votre patient(e) et lancez le traitement.')
    # 5 champs pour la saisie des données
    data1 = st.text_input("Donnée 1")
    data2 = st.text_input("Donnée 2")
    data3 = st.text_input("Donnée 3")
    data4 = st.text_input("Donnée 4")
    data5 = st.text_input("Donnée 5")
    # Bouton pour lancer le traitement des données
    if st.button("Lancer le traitement"):
        # Ajoutez ici le code pour traiter les données du cancer du sein
        st.write("Traitement en cours...")
# Boutons dans la sidebar à gauche
selected_page = st.sidebar.radio("Navigation", ["Accueil", "Maladies cardiaques", "Maladies du foie", "Maladie rénale chronique", "Diabète", "Cancer du sein"])
# Contenu des boutons
if selected_page == "Accueil":
    # Texte principal en gras
    st.write("""
    # **Bienvenue dans votre application de prédiction et de prévention des risques liés à la santé.**
    Cette plateforme vous offre la possibilité de saisir les biomarqueurs de vos patients afin d'évaluer leur risque de développer diverses pathologies, telles que le cancer du sein, les maladies cardio-vasculaires, le diabète, les affections hépatiques ou les maladies rénales chroniques.
    Cette prédiction concernant les probabilités de développement de ces maladies ne saurait en aucun cas remplacer votre avis de professionnel de la santé et n'a vocation qu'à vous aider dans la prise de décisions pour d'éventuels examens complémentaires.
    Les données que vous saisissez sont entièrement anonymisées et ne sont pas conservées, en stricte conformité avec le Règlement Général de Protection des Données (RGPD).""")
elif selected_page == "Maladies cardiaques":
    maladies_cardiaques()
elif selected_page == "Maladies du foie":
    maladies_du_foie()
elif selected_page == "Maladie rénale chronique":
    maladie_renale_chronique()
elif selected_page == "Diabète":
    diabete()
elif selected_page == "Cancer du sein":
    cancer_du_sein()







