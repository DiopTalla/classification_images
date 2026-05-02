import streamlit as st
import requests
from PIL import Image

API_URL = "http://127.0.0.1:5000"

st.title("🐶🐱 Classification Chat vs Chien")

uploaded_file = st.file_uploader("Choisir une image", type=["jpg", "png", "jpeg"])


def api_available() -> bool:
    try:
        response = requests.get(f"{API_URL}/")
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


if not api_available():
    st.warning("Le service Flask n'est pas démarré sur http://127.0.0.1:5000. Lancez `python ap.py` dans un autre terminal.")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # st.image(image, caption="Image chargée", use_column_width=True)
    st.image(image, width=300)

    if st.button("Prédire"):
        if not api_available():
            st.error("Impossible de joindre l'API Flask. Assurez-vous que `python ap.py` est en cours d'exécution.")
        else:
            with st.spinner("Analyse en cours..."):
                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        uploaded_file.type or "image/jpeg"
                    )
                }
                response = requests.post(f"{API_URL}/predict", files=files)

                if response.status_code == 200:
                    result = response.json()
                    st.success(f"Classe : {result['classe']}")
                    st.info(f"Confiance : {result['confiance']}")
                else:
                    st.error(f"Erreur lors de la prédiction ({response.status_code})")
                    st.write(response.text)