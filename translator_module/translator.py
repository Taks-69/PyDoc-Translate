from googletrans import Translator

translator_inst = Translator()

def quick_translate(text, target_lang="en"):
    """
    Traduit 'text' dans la langue 'target_lang'.
    Si la traduction est invalide (None, erreur...), renvoie le texte d'origine.
    """
    try:
        result = translator_inst.translate(text, dest=target_lang)
        if result and result.text:
            return result.text
    except:
        pass
    return text
