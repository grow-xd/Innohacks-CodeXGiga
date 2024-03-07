from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_path = r'C:\Users\PARAM\Desktop\download.jpeg'
image = Image.open(image_path)

extracted_text = pytesseract.image_to_string(image)
filtered_text = ' '.join(word for word in extracted_text.split() if word.isalpha())
print("Extracted Text:", filtered_text)