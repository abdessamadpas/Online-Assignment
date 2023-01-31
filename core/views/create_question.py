from django.http import JsonResponse
from django.shortcuts import render, redirect
from core.models import Question, Answer
import json

from core.models.exam import Exam



def create_question(request):
    if request.method == 'POST':
            body = json.loads(request.body.decode())
            id_exam = body[0]['id_exam']
            question = body[0]['question']
            new_answers = body[0]['new_answers']
            exam = Exam.objects.get(id=id_exam)
            if len(new_answers) == 0:
                # create question only if there are no answers
                q = Question(question=question, exam_id=exam)
                q.save()
            else:
                # create question with answers
                q = Question(question=question, exam_id=exam)
                q.save()
                for ans in new_answers:
                    a = Answer(answer=ans['answerValue'],question_id=q, is_correct=ans['isChecked'])
                    a.save()
            return JsonResponse({"message":"Answers created successfully"})
    else:
           return JsonResponse({"message":"Answers created successfully"})