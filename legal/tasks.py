import celery
from django.apps import apps
from acrylic.celery import app
from legal.sign import send_signature_request_for_ownership_validation



@app.task
def request_signatures_task(split_sheet_id):
    SplitSheet = apps.get_model('legal', 'SplitSheet')
    try:
        split_sheet = SplitSheet.objects.get(id=split_sheet_id)
    except SplitSheet.DoesNotExist:
        pass
    else:
        send_signature_request_for_ownership_validation(split_sheet)
    return True
