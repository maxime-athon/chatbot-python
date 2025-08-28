import customtkinter as ctk


#fonction de reponse du chatbot
def chat_reponse(user_input):
    reponses = {
        "bonjour": "👋 Bonjour ! Comment puis-je t’aider aujourd’hui ?",
        "qui est maxime": "🧑‍💻 ATHON Maxime est un passionné de développement web et attaché à la parole de Dieu.",
        "ok": "👍 Merci, c’était un plaisir de discuter ! Si tu as d’autres questions, je suis là 😊",
        "au revoir": "🌙 Au revoir ! Passe une excellente nuit. Salutations à Calixte et Albertine !",
        "comment vas-tu ?": "😃 Je vais bien, merci ! Et toi, comment s’est passée ta journée ?",
        "que fais-tu ?": "🚀 Je suis là, prêt à échanger avec toi ! On parle de quoi aujourd’hui ?",
        "parle-moi de toi": "🤖 Je suis ton compagnon virtuel, toujours dispo pour discuter et répondre à tes questions !",
        "quel est ton but ?": "💡 Mon but : rendre tes recherches et conversations plus fun et enrichissantes !",
        "as-tu une blague ?": "😆 Bien sûr ! Pourquoi les développeurs aiment le café ? Parce qu’ils ne perdent jamais la mémoire vive !",
        "dis-moi quelque chose d'intéressant": "🐙 Savais-tu qu’un poulpe a trois cœurs et du sang bleu ? Fascinant, non ?",
        "quelle est ta couleur préférée ?": "🎨 Je n’ai pas de préférence, mais le bleu est élégant et apaisant !",
        "peux-tu me motiver ?": "💪 Chaque jour est une nouvelle chance d’avancer et de briller. Tu peux le faire !"
    }
    return reponses.get(user_input.lower(), "Sory I don't hear you well")

#fonction pour genrer l'envoi de message
def send_message(event=None):
    user_message = user_input.get()
    if user_message.strip() != "":
        chat_history.configure(state="normal")
        chat_history.insert("end", f"vous: {user_message}\n", "user")
        bot_response = chat_reponse(user_message)
        chat_history.insert("end", f"chatbot: {bot_response}\n", "bot")
        chat_history.configure(state="disabled")
        chat_history.see("end")
        user_input.delete(0, "end")


#configurer l'interface graphique

custom_font = ("Segoe UI", 14)
header_font = ("Segoe UI", 20, "bold")
button_font = ("Segoe UI", 14, "bold")

app = ctk.CTk()
app.geometry("500x600")
app.title("my chatbot")  #titre

# En-tete
header = ctk.CTkLabel(app, text="Bienvenue sur le chatbot de ATHON", font=header_font)
header.pack(pady=10)


# Ajouter un effet de survol sur le bouton Envoyer
def on_enter(e):
    send_button.configure(fg_color="#2563eb")  # bleu plus foncé

def on_leave(e):
    send_button.configure(fg_color="#3b82f6")  # bleu normal

# Ajouter un raccourci clavier pour effacer le champ de saisie (Ctrl+E)
def clear_input(event=None):
    user_input.delete(0, "end")

app.bind("<Control-e>", clear_input)


ctk.set_appearance_mode("light")  # Mode clair pour un look lumineux
ctk.set_default_color_theme("blue")  # Thème de couleur principal

# Style personnalisé pour les widgets
custom_font = ("Segoe UI", 14)
header_font = ("Segoe UI", 20, "bold")
button_font = ("Segoe UI", 14, "bold")

app = ctk.CTk()

app.geometry("500x600")
app.title("my chatbot")  #titre

# En-tete
header = ctk.CTkLabel(app, text="Bienvenue sur le chatbot de ATHON", font=("Arial", 18, "bold"))
header.pack(pady=10)

                     #Zone d'affichage des message
chat_history = ctk.CTkTextbox(app, height=400, state="disabled")
chat_history.tag_config("user", foreground="blue")
chat_history.tag_config("bot", foreground="green")
chat_history.pack(pady=10, padx=10, fill="both", expand=True)

                     #champ de saisi de l'utilisateur
user_input_frame = ctk.CTkFrame(app)
user_input_frame.pack(pady=10, fill="x", padx=10)

user_input = ctk.CTkEntry(user_input_frame, placeholder_text="Entrez votre message ici.......", width=350)
user_input.pack(side="left", padx=5)
user_input.configure(font=custom_font)
user_input.focus_set()

send_button = ctk.CTkButton(user_input_frame, text="Envoyer", command=send_message)
send_button.pack(side="left")
send_button.configure(font=button_font)
send_button = ctk.CTkButton(user_input_frame, text="Envoyer", command=send_message)
send_button.pack(side="left")
send_button.configure(font=button_font)

# Ajouter un effet de survol sur le bouton Envoyer (après la création du bouton)
send_button.bind("<Enter>", on_enter)
send_button.bind("<Leave>", on_leave)

app.bind("<Return>", send_message)
app.mainloop()
