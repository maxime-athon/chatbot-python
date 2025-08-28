# Chatbot avec interface graphique (CustomTkinter)

Ce projet est une application de chatbot simple avec une interface graphique réalisée en Python grâce à la bibliothèque [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter). Le chatbot répond à des questions prédéfinies et propose une expérience utilisateur agréable.

## Fonctionnalités

- Interface graphique moderne et responsive
- Réponses personnalisées à des questions courantes
- Effet de survol sur le bouton d’envoi
- Raccourci clavier pour effacer le champ de saisie (`Ctrl+E`)
- Support de l’envoi de message avec la touche `Entrée`

## Installation

1. **Cloner le dépôt**  
   Clone ce projet ou copie les fichiers `Chatbot.py` et `main.py` dans un dossier.

2. **Installer les dépendances**  
   Assure-toi d’avoir Python 3.7+ installé.  
   Installe la bibliothèque CustomTkinter :
   ```sh
   pip install customtkinter
   ```

## Utilisation

Lance le chatbot avec la commande suivante :
```sh
python Chatbot.py
```

Une fenêtre s’ouvrira, tu pourras alors discuter avec le chatbot.

## Structure du projet

- `Chatbot.py` : Code principal de l’interface graphique et de la logique du chatbot
- `main.py` : Exemple de script Python simple (non utilisé par le chatbot)
- `.idea/` : Fichiers de configuration de l’environnement de développement (PyCharm)

## Personnalisation

Tu peux modifier les réponses du chatbot en éditant le dictionnaire `reponses` dans la fonction `chat_reponse` du fichier [`Chatbot.py`](Chatbot.py).

## Auteur

- ATHON Maxime

---
*Projet réalisé à des fins d’apprentissage et de démonstration.*
