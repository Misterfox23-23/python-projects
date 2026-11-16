# Version améliorée avec gestion des erreurs
import random

def jouer():
    nombre_secret = random.randint(1, 100)
    tentatives = 0
    print("Bienvenue dans le jeu 'Devine le nombre' !")
    print("J'ai choisi un nombre entre 1 et 100.")
    
    while True:
        try:
            choix = int(input("Votre proposition : "))
            tentatives += 1
            if choix < nombre_secret:
                print("C'est plus grand !")
            elif choix > nombre_secret:
                print("C'est plus petit !")
            else:
                print(f"Bravo ! Vous avez trouvé en {tentatives} tentatives.")
                break
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")

if __name__ == "__main__":
    jouer()
