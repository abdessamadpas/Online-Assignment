import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from core.models.answer import Answer

def delete_answers(request):
    if request.method == 'POST':
        answers_id = json.loads(request.body)
        
        answers = Answer.objects.filter(pk__in=answers_id)
        answers.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})
