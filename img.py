from PIL import Image
import pytesseract
import urllib.request 
from text_translate import new_translator
from io import BytesIO
import requests

def img_analyze(imgurl):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image_path = imgurl
    response = requests.get(imgurl)
    image_data = BytesIO(response.content)
    image = Image.open(image_data)

    extracted_text = pytesseract.image_to_string(image)
    if extracted_text=="":
        return "No text found"
    new = new_translator(extracted_text)

    return new
