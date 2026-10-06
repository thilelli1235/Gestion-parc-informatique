import tkinter as tk
from tkinter import ttk, messagebox

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion du Parc Informatique")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f5f7fa")
        
        self.colors = {
            "primary": "#7ba2dd",      
            "secondary": "#7ba2dd",    
            "success":  "#7ba2dd",      
            "warning":  "#7ba2dd",      
            "danger":  "#7ba2dd",       
            "light": "#ffffff",       
            "lighter": "#f8f9fa",      
            "border": "#d1d9e6",       
            "text": "#2c3e50",        
            "text_light": "#7b8a8b",  
            "background": "#f5f7fa",  
            "header": "#4a6fa5"       
        }
        
        
        self._configurer_styles()
        self._creer_interface()
        self._centrer_fenetre()
    
    def _configurer_styles(self):
        """Configure les styles Tkinter"""
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Primary.TButton',
            font=('Segoe UI', 10, 'bold'),
            padding=10,
            borderwidth=1,
            relief='raised',
            background=self.colors["primary"],
            foreground='white',
            bordercolor=self.colors["border"],
            focuscolor='none'
        )
        style.map('Primary.TButton',
            background=[('active', self.colors["secondary"])],
            relief=[('pressed', 'sunken')]
        )
        
        style.configure('Success.TButton',
            font=('Segoe UI', 10, 'bold'),
            padding=10,
            borderwidth=1,
            relief='raised',
            background=self.colors["success"],
            foreground='white'
        )
        
        style.configure('Warning.TButton',
            font=('Segoe UI', 10, 'bold'),
            padding=10,
            borderwidth=1,
            relief='raised',
            background=self.colors["warning"],
            foreground='white'
        )
        
        style.configure('Danger.TButton',
            font=('Segoe UI', 10, 'bold'),
            padding=10,
            borderwidth=1,
            relief='raised',
            background=self.colors["danger"],
            foreground='white'
        )
        
        style.configure('Secondary.TButton',
            font=('Segoe UI', 10, 'bold'),
            padding=10,
            borderwidth=1,
            relief='raised',
            background=self.colors["secondary"],
            foreground='white'
        )
        
        style.configure('Card.TLabelframe',
            background=self.colors["light"],
            foreground=self.colors["text"],
            borderwidth=2,
            relief='groove',
            bordercolor=self.colors["border"]
        )
        
        style.configure('Card.TLabelframe.Label',
            font=('Segoe UI', 11, 'bold'),
            background=self.colors["light"],
            foreground=self.colors["primary"]
        )
        
        style.configure('Custom.Treeview',
            background=self.colors["light"],
            foreground=self.colors["text"],
            fieldbackground=self.colors["light"],
            borderwidth=1,
            relief='solid',
            font=('Segoe UI', 10),
            rowheight=25
        )
        
        style.configure('Custom.Treeview.Heading',
            background=self.colors["primary"],
            foreground='white',
            relief='raised',
            borderwidth=1,
            font=('Segoe UI', 10, 'bold')
        )
        
        style.configure('TCombobox',
            fieldbackground=self.colors["light"],
            background=self.colors["light"],
            foreground=self.colors["text"],
            borderwidth=1,
            relief='solid'
        )
    
    def _creer_interface(self):
        """Crée toute l'interface"""
      
        main_frame = tk.Frame(self.root, bg=self.colors["background"])
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
       
        self._creer_en_tete(main_frame)
        
    
        content_frame = tk.Frame(main_frame, bg=self.colors["background"])
        content_frame.pack(fill='both', expand=True, pady=10)
        
        # Formulaire (gauche)
        form_frame = self._creer_formulaire(content_frame)
        form_frame.pack(side='left', fill='y', padx=(0, 10))
        
        # Tableau et recherche (droite)
        right_frame = tk.Frame(content_frame, bg=self.colors["background"])
        right_frame.pack(side='right', fill='both', expand=True)
        
        
        search_frame = self._creer_recherche(right_frame)
        search_frame.pack(fill='x', pady=(0, 10))
        
       
        table_frame = self._creer_tableau(right_frame)
        table_frame.pack(fill='both', expand=True)
        
        # Boutons d'action
        self._creer_boutons(main_frame)
        
        
        self._creer_barre_statut(main_frame)
    
    def _creer_en_tete(self, parent):
        """Crée l'en-tête"""
        header_frame = tk.Frame(parent, bg=self.colors["header"], height=70)
        header_frame.pack(fill='x', pady=(0, 10))
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="GESTION DU PARC INFORMATIQUE",
            font=('Segoe UI', 20, 'bold'),
            bg=self.colors["header"],
            fg='white'
        ).pack(expand=True)
    
    def _creer_formulaire(self, parent):
        """Crée le formulaire"""
        form_frame = ttk.LabelFrame(
            parent,
            text="Formulaire Équipement",
            style='Card.TLabelframe',
            width=300
        )
        form_frame.pack_propagate(False)
        
        form_content = tk.Frame(form_frame, bg=self.colors["light"], padx=15, pady=15)
        form_content.pack(fill='both', expand=True)
        
        #
        fields = [
            ("Type:", "type", "Combobox", ["PC", "Portable", "Imprimante", "Routeur", "Écran", "Serveur", "Tablette"]),
            ("Marque:", "marque", "Entry", None),
            ("Modèle:", "modele", "Entry", None),
            ("N° de série:", "serie", "Entry", None),
            ("Localisation:", "localisation", "Entry", None),
            ("État:", "etat", "Combobox", ["Opérationnel", "En panne", "Hors service", "Prêté"])
        ]
        
        self.form_widgets = {}
        
        for i, (label, field_name, widget_type, values) in enumerate(fields):
           
            tk.Label(
                form_content,
                text=label,
                font=('Segoe UI', 10),
                bg=self.colors["light"],
                fg=self.colors["text"],
                anchor='w'
            ).grid(row=i, column=0, sticky='w', pady=8, padx=(0, 10))
            
            
            if widget_type == "Combobox":
                widget = ttk.Combobox(
                    form_content,
                    values=values,
                    state='readonly',
                    font=('Segoe UI', 10),
                    width=20
                )
                widget.set(values[0])
            else:
                widget = tk.Entry(
                    form_content,
                    font=('Segoe UI', 10),
                    bg='white',
                    relief='solid',
                    borderwidth=1,
                    width=23
                )
            
            widget.grid(row=i, column=1, sticky='ew', pady=8)
            self.form_widgets[field_name] = widget
        
       
        form_content.grid_columnconfigure(1, weight=1)
        btn_reset = tk.Button(
            form_content,
            text="Réinitialiser",
            font=('Segoe UI', 9),
            bg=self.colors["text_light"],
            fg='white',
            relief='raised',
            padx=10,
            pady=5,
            cursor='hand2'
        )
        btn_reset.grid(row=len(fields), column=0, columnspan=2, pady=(20, 0))
        self.btn_reset = btn_reset
        
        return form_frame
    
    def _creer_recherche(self, parent):
        """Crée la section recherche"""
        search_frame = ttk.LabelFrame(
            parent,
            text="Recherche",
            style='Card.TLabelframe'
        )
        
        search_content = tk.Frame(search_frame, bg=self.colors["light"], padx=10, pady=10)
        search_content.pack(fill='x')
        
        tk.Label(
            search_content,
            text="Critère:",
            font=('Segoe UI', 10),
            bg=self.colors["light"],
            fg=self.colors["text"]
        ).pack(side='left', padx=(0, 10))
        
        self.search_critere = ttk.Combobox(
            search_content,
            values=["Type", "Localisation", "État", "N° de série"],
            state='readonly',
            font=('Segoe UI', 10),
            width=15
        )
        self.search_critere.set("Type")
        self.search_critere.pack(side='left', padx=(0, 20))
        
        tk.Label(
            search_content,
            text="Valeur:",
            font=('Segoe UI', 10),
            bg=self.colors["light"],
            fg=self.colors["text"]
        ).pack(side='left', padx=(0, 10))
        
        self.search_value = tk.Entry(
            search_content,
            font=('Segoe UI', 10),
            width=25,
            bg='white',
            relief='solid',
            borderwidth=1
        )
        self.search_value.pack(side='left', padx=(0, 15))
        
        self.btn_rechercher = ttk.Button(
            search_content,
            text="Rechercher",
            style='Primary.TButton'
        )
        self.btn_rechercher.pack(side='left')
        
        return search_frame
    
    def _creer_tableau(self, parent):
        """Crée le tableau"""
        table_frame = ttk.LabelFrame(
            parent,
            text="Liste des Équipements",
            style='Card.TLabelframe'
        )
        
        
        table_container = tk.Frame(table_frame, bg=self.colors["light"])
        table_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        
        table_container.grid_rowconfigure(0, weight=1)
        table_container.grid_columnconfigure(0, weight=1)
        
        # Création du Treeview
        columns = ("Type", "Marque", "Modèle", "N° Série", "Localisation", "État")
        self.tree = ttk.Treeview(
            table_container,
            columns=columns,
            show='headings',
            style='Custom.Treeview',
            height=12
        )
        
        
        col_widths = [100, 100, 120, 120, 100, 100]
        for col, width in zip(columns, col_widths):
            self.tree.heading(col, text=col, anchor='w')
            self.tree.column(col, width=width, anchor='w', minwidth=80)
        
       
        vsb = ttk.Scrollbar(table_container, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        
        
        self.tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        
        return table_frame
    
    def _creer_boutons(self, parent):
        buttons_frame = tk.Frame(parent, bg=self.colors["background"])
        buttons_frame.pack(fill='x', pady=10)
        
        buttons = [
            ("Ajouter", 'Success.TButton', "btn_ajouter"),
            ("Modifier", 'Warning.TButton', "btn_modifier"),
            ("Supprimer", 'Danger.TButton', "btn_supprimer"),
            ("Afficher tout", 'Secondary.TButton', "btn_afficher_tout"),
            ("Quitter", 'Danger.TButton', "btn_quitter")
        ]
        
        for text, style_name, attr_name in buttons:
            btn = ttk.Button(
                buttons_frame,
                text=text,
                style=style_name
            )
            btn.pack(side='left', padx=5)
            setattr(self, attr_name, btn)
    
    def _creer_barre_statut(self, parent):
        status_frame = tk.Frame(parent, bg=self.colors["text_light"], height=30)
        status_frame.pack(fill='x')
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text="Prêt - 0 équipement(s)",
            font=('Segoe UI', 9),
            bg=self.colors["text_light"],
            fg='white'
        )
        self.status_label.pack(side='left', padx=10)
        
        sql_label = tk.Label(# Ajouter un label pour le fichier SQLite
            status_frame,
            text="Base de données: parc_informatique.db",
            font=('Segoe UI', 9),
            bg=self.colors["text_light"],
            fg='white'
        )
        sql_label.pack(side='right', padx=10)
    
    def _centrer_fenetre(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    
    def get_inputs(self):
        return (
            self.form_widgets['type'].get(),
            self.form_widgets['marque'].get(),
            self.form_widgets['modele'].get(),
            self.form_widgets['serie'].get(),
            self.form_widgets['localisation'].get(),
            self.form_widgets['etat'].get()
        )
    
    def set_inputs(self, equipement):
        if equipement:
            self.form_widgets['type'].set(equipement[0])
            self.form_widgets['marque'].delete(0, tk.END)
            self.form_widgets['marque'].insert(0, equipement[1])
            self.form_widgets['modele'].delete(0, tk.END)
            self.form_widgets['modele'].insert(0, equipement[2])
            self.form_widgets['serie'].delete(0, tk.END)
            self.form_widgets['serie'].insert(0, equipement[3])
            self.form_widgets['localisation'].delete(0, tk.END)
            self.form_widgets['localisation'].insert(0, equipement[4])
            self.form_widgets['etat'].set(equipement[5])
    
    def clear_form(self):
        for widget in self.form_widgets.values():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)
            elif isinstance(widget, ttk.Combobox):
                if widget['values']:
                    widget.set(widget['values'][0])
    
    def afficher_liste(self, equipements):
        self.tree.delete(*self.tree.get_children())
        
        for i, eq in enumerate(equipements):
            tag = 'even' if i % 2 == 0 else 'odd'
            self.tree.insert('', 'end', values=eq, tags=(tag,))
        
        count = len(equipements) # Mettre à jour le statut
        self.status_label.config(text=f"Prêt - {count} équipement(s) affiché(s)")
    
    def get_selected_equipement(self):
        selection = self.tree.selection()
        if selection:
            return self.tree.item(selection[0], 'values')
        return None
    
    def get_critere_recherche(self):
        mapping = {
            "Type": "type",
            "Localisation": "localisation",
            "État": "etat",
            "N° de série": "serie"
        }
        return mapping.get(self.search_critere.get(), "type")
    
    def get_valeur_recherche(self):
        return self.search_value.get().strip()
    
    def message_info(self, titre, message):
        messagebox.showinfo(titre, message)
    
    def message_erreur(self, titre, message):
        messagebox.showerror(titre, message)
    
    def demander_confirmation(self, titre, message):
        return messagebox.askyesno(titre, message)