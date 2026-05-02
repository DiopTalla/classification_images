#  📌 📖 Description du projet

Ce projet consiste à développer une application de classification d’images capable de distinguer automatiquement les chats et les chiens à l’aide des techniques de deep learning.

Le modèle repose sur un réseau de neurones convolutif basé sur le transfert learning avec l’architecture MobileNetV2.

L’application est déployée sous forme d’une architecture microservices, comprenant :

une API de prédiction avec Flask
une interface utilisateur interactive avec Streamlit
# 🎯 Objectifs
Construire un modèle performant de classification d’images
Exploiter le transfert learning
Interpréter les décisions du modèle avec Grad-CAM
Déployer le modèle sous forme d’API
Concevoir une interface utilisateur intuitive

# 🧠 Technologies utilisées
Python
TensorFlow / Keras
Flask
Streamlit
NumPy
OpenCV
Matplotlib

# 🧪 Fonctionnement
L’utilisateur charge une image via l’interface Streamlit
L’image est envoyée à l’API Flask
Le modèle prédit la classe (chat ou chien)
Le résultat est affiché avec un niveau de confiance

# 📊 Performances du modèle
Accuracy : ~96%
Loss : faible
Bonne généralisation (pas d’overfitting)

# 🔍 Explicabilité

Le modèle intègre la technique Grad-CAM, permettant de :
visualiser les zones importantes de l’image
interpréter les décisions du modèle
valider la pertinence des prédictions
📦 Sauvegarde des artefacts

# Le projet inclut :

modèle entraîné (.keras)
classes (classes.json)
configuration de prétraitement
historique d’entraînement
🏗️ Architecture

# Le système suit une architecture microservices :

API Flask → prédiction
Interface Streamlit → interaction utilisateur
🚀 Améliorations possibles
Déploiement sur cloud (AWS, Azure)
Dockerisation
Passage à FastAPI
Ajout d’autres classes (multi-classe)
 # 👨‍💻 Auteur

Projet réalisé par : Talla Diop
Master Intelligence artificielle et smatech 
