from googletrans import Translator

def translate_text(text, src_lang='kn', dest_lang='en'):
    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated_text.text

# Example usage:
kannada_text = "ನಮಸ್ತೆ, ಈ ಒಂದು ಉಹರಣೆ ಕೆಲಸ ಮಾಡಿದ್ದೇನೆ."
translated_text = translate_text(kannada_text)
print("Translated text:", translated_text)
