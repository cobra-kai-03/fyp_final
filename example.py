# import requests
# from bs4 import BeautifulSoup

# def translate_text(text, src_lang='kn', dest_lang='en'):
#     # Define the URL for Google Translate
#     url = "https://translate.google.com/"
    
#     # Prepare the payload data
#     data = {
#         "sl": src_lang,  # Source language
#         "tl": dest_lang,  # Destination language
#         "text": text,  # Text to translate
#         "op": "translate"  # Operation
#     }
    
#     # Send a POST request to Google Translate
#     response = requests.post(url, data=data)
    
#     # Parse the HTML response
#     soup = BeautifulSoup(response.content, "html.parser")
    
#     # Find the translated text element
#     translation_span = soup.find("span", {"class": "tlid-translation translation"})
    
#     # Check if the translation element exists
#     if translation_span:
#         translated_text = translation_span.text
#     else:
#         translated_text = "Translation not found"
    
#     return translated_text

# # Example usage
# text_to_translate = "ನಮಸ್ತೆ, ಈ ಒಂದು ಉದಾಹರಣೆ ಕೆಲಸ ಮಾಡಿದ್ದೇನೆ."
# translated_text = translate_text(text_to_translate, src_lang='kn', dest_lang='en')
# print("Translated text:", translated_text)

import easyocr
# Initialize the OCR reader with the language parameter set to 'kn' for Kannada
reader = easyocr.Reader(['kn'])

# Load the Kannada image
image_path = 'test2.jpg'

# Perform OCR on the image
result = reader.readtext(image_path)

# Extract text from the OCR result
kannada_text = ' '.join([entry[1] for entry in result])

# Print the extracted Kannada text
print("Extracted Kannada Text:", kannada_text)