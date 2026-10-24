assistant.py
print("=== ASSISTANT FIRMIN ===")

nom = input("Comment tu t'appelles ? ")

choix = input("Tu préfères la médecine ou l'informatique ? ")

choix = choix.lower()

if choix == "médecine":
    print("Bonjour " + nom + ", futur médecin !")

elif choix == "informatique":
    print("Bonjour " + nom + ", futur développeur !")

else:
    print("Bonjour " + nom + ", ton choix est intéressant !")
