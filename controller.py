class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        # Lier les boutons
        self.view.btn_ajouter.config(command=self.ajouter)
        self.view.btn_modifier.config(command=self.modifier)
        self.view.btn_supprimer.config(command=self.supprimer)
        self.view.btn_rechercher.config(command=self.rechercher)
        self.view.btn_afficher_tout.config(command=self.afficher_tout)
        self.view.btn_quitter.config(command=self.quitter)
        self.view.btn_reset.config(command=self.reset_form)
        self.view.tree.bind('<<TreeviewSelect>>', self.on_select)# Lier la sélection dans le tableau
        self.view.search_value.bind('<Return>', lambda e: self.rechercher()) # Lier la touche Entrée pour la recherche
        self.afficher_tout()# Afficher tous les équipements au démarrage
        self.afficher_statistiques()# Afficher les statistiques
    
    def ajouter(self):
        equipement = self.view.get_inputs()
        
       
        if not self._valider_equipement(equipement):
            return
        
        
        if self.model.verifier_serie_existe(equipement[3]):
            self.view.message_erreur(
                "Erreur",
                "Numéro de série déjà existant."
            )
            return
        
       
        if self.model.ajouter_equipement(equipement):
            self.view.message_info(
                "OK",
                "Équipement ajouté."
            )
            self.reset_form()
            self.afficher_tout()
            self.afficher_statistiques()
        else:
            self.view.message_erreur("Erreur", "Impossible d'ajouter l'équipement")
    
    def modifier(self):
        
        equipement_selectionne = self.view.get_selected_equipement()
        if not equipement_selectionne:
            self.view.message_erreur("Erreur", "Veuillez sélectionner un équipement à modifier")
            return
        
        nouvelles_donnees = self.view.get_inputs()
        
       
        if not self._valider_equipement(nouvelles_donnees):
            return
        
        if equipement_selectionne[3] != nouvelles_donnees[3]:
            if self.model.verifier_serie_existe(nouvelles_donnees[3]):
                self.view.message_erreur(
                    "Erreur",
                    "Ce numéro de série existe déjà. Veuillez en choisir un autre."
                )
                return
        
        if self.model.modifier_equipement(nouvelles_donnees):
            self.view.message_info("Succès", "Équipement modifié avec succès")
            self.afficher_tout()
            self.afficher_statistiques()
        else:
            self.view.message_erreur("Erreur", "Impossible de modifier l'équipement")
    
    def supprimer(self):
        equipement = self.view.get_selected_equipement()
        if not equipement:
            self.view.message_erreur("Erreur", "Veuillez sélectionner un équipement à supprimer")
            return
        
        
        if not self.view.demander_confirmation(
            "Suppression",
            "Confirmer la suppression ?"
        ):
            return
        
        self.model.supprimer_equipement(equipement[3])
        self.view.message_info("Succès", "Équipement supprimé")
        self.reset_form()
        self.afficher_tout()
        self.afficher_statistiques()
    
    def rechercher(self):
        critere = self.view.get_critere_recherche()
        valeur = self.view.get_valeur_recherche()
        
        if not valeur:
            self.view.message_erreur("Erreur", "Veuillez saisir une valeur de recherche")
            return
        
        resultats = self.model.rechercher_equipement(critere, valeur)
        
        if not resultats:
            self.view.message_info("Information", "Aucun équipement trouvé")
        
        self.view.afficher_liste(resultats)
    
    def afficher_tout(self):
        equipements = self.model.afficher_tous()
        self.view.afficher_liste(equipements)
    
    def reset_form(self):
       self.view.clear_form()
    
    def on_select(self, event=None):
        equipement = self.view.get_selected_equipement()
        if equipement:
            self.view.set_inputs(equipement)
    
    def afficher_statistiques(self):
        stats = self.model.obtenir_statistiques()
        print(f"Statistiques de la base: {stats['total_equipements']} équipements, {stats['nombre_types']} types")
    
    def exporter_sql(self):
        fichier = self.model.exporter_sql()
        self.view.message_info(
            "Export réussi",
            f"Base de données exportée dans:\n{fichier}"
        )
    
    def _valider_equipement(self, equipement):
        errors = []
        
        if not equipement[0]:  
            errors.append("Le type est obligatoire")
        
        if not equipement[1]:  
            errors.append("La marque est obligatoire")
        
        if not equipement[2]:  
            errors.append("Le modèle est obligatoire")
        
        if not equipement[3]:  
            errors.append("Le numéro de série est obligatoire")
        
        if not equipement[4]:  
            errors.append("La localisation est obligatoire")
        
        if not equipement[5]: 
            errors.append("L'état est obligatoire")
        
        if errors:
            self.view.message_erreur(
                "Erreur de validation",
                "Veuillez remplir tous les champs obligatoires."
            )
            return False
        
        return True
    
    def quitter(self):
        self.exporter_sql() # Exporter la base avant de quitter
        
        if self.view.demander_confirmation(
            "Quitter",
            "Voulez-vous vraiment quitter l'application ?"
        ):
            self.model.fermer()
            self.view.root.quit()