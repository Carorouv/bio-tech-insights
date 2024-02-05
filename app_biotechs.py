

from st_on_hover_tabs import on_hover_tabs
import streamlit as st
import os
import base64

st.set_page_config(layout="wide")

#st.header("Custom tab component for on-hover navigation bar")




# Mise en place du background de l'appli
#def set_bg_hack_url():
    # Remplacez l'URL ci-dessous par l'URL directe de votre image hébergée sur le web
    # image_url = "https://media2.ledevoir.com/images_galerie/nwd_1589764_1231201/image.jpg"
    # st.markdown(
    #      f"""
    #      <style>
    #      .stApp {{
    #          background: url("{image_url}");
    #          background-size: cover;
             
    #      }}
    #      </style>
    #      """,
    #      unsafe_allow_html=True
    #  )
# set_bg_hack_url()



# Chemin vers l'image dans le même dossier que votre code
image_path = "medical_wallpaper_2.jpg"

page_bg_img = '''
<style>
body {
background-image: url("{image_path}");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)





with st.sidebar:
    tabs = on_hover_tabs(tabName=['Accueil', 'Diabète', 'Cancer du sein', 'Maladie du foie', 'Maladies cardiaques', 'Maladie rénale chronique' ], 
                         iconName=['accueil', 'diabète', 'cancer du sein', 'maladie du foie', 'maladies cardiaques', 'maladie rénale chronique'], default_choice=0)
   
if tabs =='Accueil':
    st.title("Accueil")
    st.write("Bienvenue dans notre application de prédiction et de prévention des risques liés à la santé.")
    st.write("Cette plateforme vous offre la possibilité de saisir vos propres bio-marqueurs ou ceux de vos patients afin d'évaluer le risque de développer diverses pathologies, telles que le cancer du sein, les maladies cardio-vasculaires, le diabète, les affections hépatiques ou les maladies rénales chroniques.\n\nIl est important de souligner que cette prédiction concernant les probabilités de développement de ces maladies ne saurait en aucun cas remplacer l'avis d'un professionnel de la santé. \n\nNous tenons à vous assurer que vos données sont entièrement anonymisées et ne sont pas conservées, en stricte conformité avec le Règlement Général de Protection des Données (RGPD).")

   

elif tabs == 'Diabète':
    st.title("Diabète")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Cancer du sein':
    st.title("Cancer du sein")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Maladie du foie':
    st.title("Maladie du foie")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Maladies cardiaques':
    st.title("Maladies cardiaques")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Maladie rénale chronique':
    st.title("Maladie rénale chronique")
    st.write('Name of option is {}'.format(tabs))
    