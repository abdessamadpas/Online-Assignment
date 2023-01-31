import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from core.models.answer import Answer

def update_answers(request):
  if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
       
        for answer_data in data:
            answer = get_object_or_404(Answer, pk=answer_data['answerId'])
            answer.answer = answer_data['answerValue']
            answer.is_correct = answer_data['isChecked']
            answer.save()
        
  return JsonResponse({'message': 'Answers updated successfully'})
