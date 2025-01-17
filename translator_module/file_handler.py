# file_handler.py
import os

def get_python_files(path):
    """
    Retourne une liste des fichiers .py si 'path' est un fichier unique .py
    ou tous les fichiers .py d'un dossier si 'path' est un dossier.
    """
    if os.path.isfile(path) and path.endswith('.py'):
        return [path]
    elif os.path.isdir(path):
        all_files = []
        for f in os.listdir(path):
            full_path = os.path.join(path, f)
            if os.path.isfile(full_path) and f.endswith('.py'):
                all_files.append(full_path)
        return all_files
    return []

