print("=== JARVIS DE FIRMIN ===")

nom = input("Comment t'appelles-tu ? ")

print("Bonjour", nom, "!")
print("Je suis JARVIS, ton assistant personnel.")

while True:
    commande = input("Que puis-je faire pour toi ? ")

    if commande.lower() == "bonjour":
        print("Bonjour ! Je suis à ton service.")

    elif commande.lower() == "qui es-tu":
        print("Je suis JARVIS, ton assistant personnel.")

    elif commande.lower() == "medecine":
        print("Je peux t'aider à réviser tes cours de médecine.")

    elif commande.lower() == "stop":
        print("À bientôt, chef !")
        break

    else:
        print("Je ne connais pas encore cette commande.")
