import json
from PIL import Image
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
from foreignLangOCR.lib.detect import detect_hindi_tesseract, detect_hindi
from foreignLangOCR.lib.db_write import save_result_to_db


@csrf_exempt
def health_check(request):
    response = {
        'status': 'ok'
    }
    return HttpResponse(json.dumps(response), status=200, content_type='application/json')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            img = Image.open(request.FILES['file'])
            response = detect_hindi(img)
            save_result_to_db(request.FILES['file'],''.join(response))
            return render(request, 'result.html', {'success':True,'response':response})
        else:
            print(f"form is invalid, {form}")

    return render(request, 'upload.html', {'success':False})

