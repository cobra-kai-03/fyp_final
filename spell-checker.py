from spellchecker import SpellChecker

def kannada_spell_correction(text):
    spell = SpellChecker(language=None)  # Language will be detected automatically
    corrected_text = []
    words = text.split()
    for word in words:
        corrected_word = spell.correction(word)
        corrected_text.append(corrected_word)
    return ' '.join(corrected_text)

# Example usage:
kannada_text = "ನಾನು ಒಂದು ಪಸ್ತಕವನ್ನು ಓದಿದ್ದೇನೆ."
corrected_text = kannada_spell_correction(kannada_text)
print("Corrected text:", corrected_text)
