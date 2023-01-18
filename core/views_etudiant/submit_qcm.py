from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
import json

from rest_framework.decorators import api_view

# Create your views here.
from core.models import *


@api_view(['POST'])
# @login_required(login_url='login')
def submit_qcm(request, module_id, exam_id):
    user = request.user
    #! check if user is student or not to access this page
    print("dashboard admin  page user is", user)
    if user.is_staff:
        return redirect('access_denied_student')

    exam = get_object_or_404(Exam, id=exam_id)
    earned_points = 0
    if request.method == 'POST':
        # print("request.body.decode()",request.body.decode())
        questions = request.data.get("questions")
        answers = request.data.get("answers")
        print("questions", questions)
        print("answers", answers)
        attempter = Attempter.objects.create(user=user, exam=exam, score=0)
        
        for qst, anw in zip(questions, answers):
            question = Question.objects.get(id=qst)
            answer_object = Answer.objects.get(answer=anw)
            answer = get_object_or_404(Answer, id=answer_object.id)
            Attempt.objects.create(exam=exam, attempter=attempter, question=question, answer=answer)
            if answer.is_correct == True:
                earned_points += question.points
                attempter.score += earned_points
                attempter.save()
           

    	#return redirect('notes', module_id=module_id, exam_id=exam_id)
        return Response({
            "questions": questions,
            "earned_points": earned_points,
            "exam_id": exam_id,
            "created": True})
    return Response({
            "lay lay": "lay klay",
           })