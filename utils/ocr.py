import pytesseract
from PIL import Image

# Đường dẫn tới tesseract.exe (nếu cần trên Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def perform_ocr(image_path):
    # Mở ảnh và trích xuất văn bản
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text
