# cli.py
import argparse
import os
from translator_module import file_handler
from translator_module.comment_extractor import replace_comments_in_file

def main():
    parser = argparse.ArgumentParser(
        description="Traduire automatiquement les commentaires et docstrings d'un fichier ou dossier .py."
    )

    parser.add_argument(
        "--path",
        "-p",
        required=True,
        help="Chemin vers un fichier .py ou un dossier contenant des .py"
    )

    parser.add_argument(
        "--lang",
        "-l",
        default="en",
        help="Langue de traduction (ex: en, fr, es, etc.). Par défaut: en"
    )

    parser.add_argument(
        "--output",
        "-o",
        default="output",
        help="Nom du dossier de sortie (par défaut: 'output')"
    )

    args = parser.parse_args()

    chosen_path = args.path.strip()
    target_lang = args.lang.strip()
    output_dir = os.path.join(os.getcwd(), args.output)

    # Vérifier que le chemin existe
    if not os.path.exists(chosen_path):
        print(f"ERREUR: Le chemin '{chosen_path}' n'existe pas.")
        return

    # Récupération de tous les fichiers .py
    py_files = file_handler.get_python_files(chosen_path)
    if not py_files:
        print(f"ERREUR: Aucun fichier .py trouvé dans '{chosen_path}'.")
        return

    # Création du dossier de sortie
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # On boucle sur chaque fichier .py
    for py_file in py_files:
        with open(py_file, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = replace_comments_in_file(content, target_lang)

        # Écriture dans le dossier de sortie
        filename = os.path.basename(py_file)
        output_path = os.path.join(output_dir, f"translated_{filename}")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(new_content)

    print(f"Traduction terminée ! Les fichiers traduits se trouvent dans '{output_dir}'.")
