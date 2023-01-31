from django.http import JsonResponse
from django.shortcuts import render, redirect ,get_object_or_404
from core.models import Answer, Question
import json

def create_answers(request):
    if request.method == 'POST':
        answers_added = json.loads(request.body)
        for answer in answers_added:
            
            question = get_object_or_404(Question, pk=answer['tableId'])
            answer_value = answer.get('answerValue')
            is_checked = answer.get('isChecked')
            new_answer = Answer.objects.create(
                answer=answer_value,
                is_correct=is_checked,
                question_id=question
            )
            new_answer.save()
        
        return JsonResponse({"message":"Answers created successfully"})
    else:
        return JsonResponse({"error":"Invalid request method"})
