import tkinter as tk
from tkinter import filedialog, messagebox
import os

from translator_module import file_handler
# On importe la fonction de remplacement depuis comment_extractor
from translator_module.comment_extractor import replace_comments_in_file

# -------------------------------------------------------------------------
# COULEURS & POLICE (THÈME SOMBRE / CYBERPUNK)
# -------------------------------------------------------------------------
PRIMARY_BG = "#1E1E1E"      # Couleur de fond principale
SECONDARY_BG = "#2E2E2E"    # Couleur de fond secondaire
PRIMARY_FG = "#C0C0C0"      # Couleur de texte principale
ACCENT_FG = "#39FF14"       # Couleur d'accent (vert)
FONT = ("Consolas", 10, "bold")


def select_path(path_mode_var, path_var):
    """
    Ouvre un dialogue pour sélectionner soit un fichier (.py), soit un dossier,
    selon la valeur de 'path_mode_var'.
    Met à jour 'path_var' pour afficher le chemin dans l'UI.
    """
    if path_mode_var.get() == "file":
        chosen_path = filedialog.askopenfilename(
            title="Choisir un fichier .py",
            filetypes=[("Fichiers Python", "*.py")]
        )
    else:
        chosen_path = filedialog.askdirectory(
            title="Choisir un dossier contenant des .py"
        )

    if chosen_path:
        path_var.set(chosen_path)
    else:
        path_var.set("")


def start_translation(path_var, lang_var):
    """
    Lance la traduction en utilisant le chemin (fichier ou dossier) dans 'path_var'
    et la langue ciblée dans 'lang_var'. Génère un dossier 'output' dans le dossier courant.
    """
    # Vérification du chemin
    chosen_path = path_var.get().strip()
    if not chosen_path:
        messagebox.showerror("Erreur", "Veuillez d'abord sélectionner un fichier ou un dossier.")
        return

    # Vérification de la langue
    target_lang = lang_var.get().strip()
    if not target_lang:
        messagebox.showerror("Erreur", "Veuillez saisir une langue (ex. en, fr, es...)")
        return

    # Récupération de tous les .py
    py_files = file_handler.get_python_files(chosen_path)
    if not py_files:
        messagebox.showerror("Erreur", "Aucun fichier .py trouvé dans le chemin sélectionné.")
        return

    # Créer un dossier 'output' dans le répertoire courant
    output_dir = os.path.join(os.getcwd(), "output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Pour chaque fichier, on lit, on traduit, on écrit
    for py_file in py_files:
        with open(py_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Remplacer les commentaires (docstrings + #) par la version traduite
        new_content = replace_comments_in_file(content, target_lang)

        # Créer le chemin de sortie
        filename = os.path.basename(py_file)
        output_path = os.path.join(output_dir, f"translated_{filename}")

        # Écrit le fichier traduit dans output/
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(new_content)

    messagebox.showinfo(
        "Succès",
        f"Traduction terminée !\nFichiers traduits dans :\n{output_dir}"
    )


def main():
    """
    Point d'entrée : Lancement de l'interface graphique.
    """
    root = tk.Tk()
    root.title("PyDoc Translate - Cyberpunk Edition")
    root.configure(bg=PRIMARY_BG)

    # Variables
    path_mode_var = tk.StringVar(value="file")  # file ou folder
    path_var = tk.StringVar(value="")
    lang_var = tk.StringVar(value="")

    # ----------------------
    # 1) Sélection Fichier / Dossier
    # ----------------------
    label_mode = tk.Label(root, text="Sélection :", bg=PRIMARY_BG, fg=PRIMARY_FG, font=FONT)
    label_mode.pack(pady=5)

    frame_radio = tk.Frame(root, bg=PRIMARY_BG)
    frame_radio.pack()

    radio_file = tk.Radiobutton(
        frame_radio,
        text="Fichier (.py)",
        variable=path_mode_var,
        value="file",
        bg=PRIMARY_BG,
        fg=PRIMARY_FG,
        selectcolor=PRIMARY_BG,
        activebackground=PRIMARY_BG,
        activeforeground=PRIMARY_FG,
        font=FONT
    )
    radio_file.pack(side="left", padx=10)

    radio_folder = tk.Radiobutton(
        frame_radio,
        text="Dossier",
        variable=path_mode_var,
        value="folder",
        bg=PRIMARY_BG,
        fg=PRIMARY_FG,
        selectcolor=PRIMARY_BG,
        activebackground=PRIMARY_BG,
        activeforeground=PRIMARY_FG,
        font=FONT
    )
    radio_folder.pack(side="left", padx=10)

    btn_select = tk.Button(
        root,
        text="Choisir le chemin",
        command=lambda: select_path(path_mode_var, path_var),
        bg=SECONDARY_BG,
        fg=ACCENT_FG,
        activebackground=PRIMARY_BG,
        activeforeground=PRIMARY_FG,
        relief="flat",
        font=FONT
    )
    btn_select.pack(pady=10, fill="x", padx=20)

    # Label pour afficher le chemin choisi
    label_path = tk.Label(root, textvariable=path_var, bg=PRIMARY_BG, fg=PRIMARY_FG, font=FONT)
    label_path.pack(pady=5)

    # ----------------------
    # 2) Saisie de la langue
    # ----------------------
    label_lang = tk.Label(
        root,
        text="Langue cible (ex: en, fr, es...):",
        bg=PRIMARY_BG,
        fg=PRIMARY_FG,
        font=FONT
    )
    label_lang.pack(pady=5)

    entry_lang = tk.Entry(
        root,
        textvariable=lang_var,
        bg=SECONDARY_BG,
        fg=PRIMARY_FG,
        insertbackground=PRIMARY_FG,
        font=FONT,
        highlightthickness=1,
        highlightbackground=ACCENT_FG,
        relief="flat"
    )
    entry_lang.pack(pady=5, padx=20, fill="x")

    # ----------------------
    # 3) Bouton de traduction
    # ----------------------
    btn_translate = tk.Button(
        root,
        text="Lancer la traduction",
        command=lambda: start_translation(path_var, lang_var),
        bg=SECONDARY_BG,
        fg=ACCENT_FG,
        activebackground=PRIMARY_BG,
        activeforeground=PRIMARY_FG,
        relief="flat",
        font=FONT
    )
    btn_translate.pack(pady=20, fill="x", padx=20)

    root.mainloop()
