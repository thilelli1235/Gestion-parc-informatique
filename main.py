import tkinter as tk
import sys  
from model import Model
from view import View
from controller import Controller

def main():
   
    print("=" * 60)
    print("SYSTÈME DE GESTION DU PARC INFORMATIQUE")
    print("=" * 60)
    print("Création de la base de données 'parc_informatique.db'...")
    
    try:
        
        root = tk.Tk()
        
        model = Model()
        
        view = View(root)
        
        controller = Controller(model, view)
        
        # Raccourcis clavier
        root.bind('<Control-s>', lambda e: controller.rechercher())
        root.bind('<Control-n>', lambda e: controller.ajouter())
        root.bind('<Control-r>', lambda e: controller.reset_form())
        root.bind('<Control-q>', lambda e: controller.quitter())
        root.bind('<F5>', lambda e: controller.afficher_tout())
        
        
        print("Base de données créée avec succès!")
        print(f"Fichier généré: parc_informatique.db")
        print("Lancement de l'interface graphique...")
        print("=" * 60)
        
        root.mainloop()
        
    except ImportError as e:
        print(f"ERREUR: Module manquant - {e}")
        print("Assurez-vous que tous les fichiers sont présents:")
        print("  - model.py")
        print("  - view.py")
        print("  - controller.py")
        input("Appuyez sur Entrée pour quitter...")
        sys.exit(1)
        
    except Exception as e:
        print(f"ERREUR inattendue: {e}")
        import traceback
        traceback.print_exc()
        input("Appuyez sur Entrée pour quitter...")
        sys.exit(1)

if __name__ == "__main__":
    main()