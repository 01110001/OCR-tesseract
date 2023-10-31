import pytesseract
from PIL import Image

# Chemin vers l'exécutable Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ouvrir une image à partir du chemin
image = Image.open('digit.jpg')

# Utiliser Tesseract pour faire de la reconnaissance de texte
text = pytesseract.image_to_string(image)

# Afficher le texte extrait
print(text)
