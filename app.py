import pytesseract
import streamlit as st
from pdf2image import convert_from_bytes
import PIL
from pytesseract import image_to_string

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def convert_pdf_to_img(pdf_file):
    return convert_from_bytes(pdf_file)

def convert_image_to_text(file):
    text = image_to_string(file)
    return text


def get_text_from_any_pdf(pdf_file):
    images = convert_pdf_to_img(pdf_file)
    final_text = " "
    for pg, img in enumerate(images):

        final_text += convert_image_to_text(img)

    return final_text

imagem_referencia = st.file_uploader("Upload File", type=["jpg", "jpeg", "png", "pdf", "tiff"])



if imagem_referencia is not None:
	pdf = get_text_from_any_pdf(imagem_referencia.read())
	st.write(pdf)









