import os
import shutil

# Script simple pour nettoyer le dossier /tmp sous Linux
def nettoyer_tmp():
    dossier = "/tmp"
    print(f"Nettoyage du dossier : {dossier}")
    
    for fichier in os.listdir(dossier):
        chemin_complet = os.path.join(dossier, fichier)
        try:
            if os.path.isfile(chemin_complet) or os.path.islink(chemin_complet):
                os.unlink(chemin_complet)
                print(f"Fichier supprimé : {fichier}")
            elif os.path.isdir(chemin_complet):
                shutil.rmtree(chemin_complet)
                print(f"Dossier supprimé : {fichier}")
        except Exception as e:
            print(f"Erreur avec {fichier} : {e}")

if __name__ == "__main__":
    nettoyer_tmp()
    print("Nettoyage terminé.")
