import re
from translator_module.translator import quick_translate

def replace_comments_in_file(file_content, target_lang):
    """
    1) Remplace d'abord les blocs triple-quotes (\"\"\"...\"\"\" ou '''...'''),
       en traduisant uniquement le texte intérieur, tout en conservant les
       délimiteurs.

    2) Ensuite, remplace les commentaires #, en traduisant uniquement
       le texte après le #.

    3) Ignore les simples "..." ou '...'.
    """

    # --- 1) Regex pour les blocs triple-quotes ---
    # group(1) = """...""" (bloc entier),   group(2) = contenu interne des """
    # group(3) = '''...''' (bloc entier),   group(4) = contenu interne des '''
    triple_pattern = r'(\"\"\"([\s\S]*?)\"\"\")|(\'\'\'([\s\S]*?)\'\'\')'

    def triple_replacer(match):
        start_index = match.start()
        line_start = file_content.rfind('\n', 0, start_index) + 1
        prefix = file_content[line_start:start_index]
        if prefix.strip():
            # Présence de contenu avant le début des triple quotes : ne pas traduire.
            return match.group(0)
        
        if match.group(1) is not None:
            content = match.group(2)  # Le texte sans les guillemets pour les """..."""
            translated = quick_translate(content, target_lang)
            return f'"""{translated}"""'
        else:
            content = match.group(4)  # Le texte sans les guillemets pour les '''...'''
            translated = quick_translate(content, target_lang)
            return f"'''{translated}'''"

    # IMPORTANT: on ajoute flags=re.DOTALL
    updated_content = re.sub(triple_pattern, triple_replacer, file_content, flags=re.DOTALL)

    # --- 2) Regex pour les commentaires # ---
    # On capture tout ce qui vient après le # (éventuel espace inclus)
    single_line_pattern = r'#\s?(.*)'

    def single_line_replacer(match):
        comment_text = match.group(1)
        translated = quick_translate(comment_text, target_lang)
        return f'# {translated}'

    updated_content = re.sub(single_line_pattern, single_line_replacer, updated_content)

    return updated_content
