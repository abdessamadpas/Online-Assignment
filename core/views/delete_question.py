from django.shortcuts import render, redirect
from core.models import Question, Answer
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404


def delete_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id_question= data.get('id_question')
        print ("id qst is :",id_question)
        question = Question.objects.get(id=id_question)
        print(question)
        answers = Answer.objects.filter(question_id=id_question)
        print(answers)
        question.delete()
        answers.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})