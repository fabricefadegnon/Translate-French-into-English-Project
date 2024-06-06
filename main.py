from deep_translator import GoogleTranslator
def translate_french_to_english(text):
    # Create a GoogleTranslator object
    translator = GoogleTranslator(source='fr', target='en')

    # Translate the text from French to English
    translation = translator.translate(text)

    # Return the translated text
    return translation


# Get user input for French text
french_text = input("Insérez un texte: ")

# Translate the French text to English
english_text = translate_french_to_english(french_text)

# Print the original French text and the translated English text
print(f"Original French: {french_text}")
print(f"Translated English: {english_text}")
