from foreignLangOCR.models import Document


def save_result_to_db(img, text):
    document = Document()
    document.image = img
    document.ocr = text
    document.save()
