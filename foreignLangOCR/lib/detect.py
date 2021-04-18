from tesserocr import PyTessBaseAPI, PSM, RIL, iterate_level
import pytesseract
from PIL import Image



class Const:
    lang = 'hin'
    psm = 3


def detect_hindi(img: Image):
    ocr_api = PyTessBaseAPI(psm=PSM.SPARSE_TEXT, lang=Const.lang)
    meta, response = [], []
    img_width, img_height = img.size
    print("started processing image")
    ocr_api.SetImage(img)
    ocr_api.Recognize()
    level = RIL.TEXTLINE
    results = ocr_api.GetIterator()
    line = 0
    for r in iterate_level(results, level):
        text = r.GetUTF8Text(level)
        text = text.replace('\n', '')
        bb = r.BoundingBox(level)
        confidence = r.Confidence(level)
        confidence = "{:.2f}".format(confidence)
        meta.append({
            'text': text,
            'confidence': confidence,
            'bb_box': bb,
            'img_width': img_width,
            'img_height': img_height,
            'line': line
        })
        response.append(text)
        line += 1

    return response


def detect_hindi_tesseract(img: Image):
    text = pytesseract.image_to_string(img, lang=Const.lang)
    response = text.split('\n')
    return response


