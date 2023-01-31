from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from rest_framework.decorators import api_view
import json

from django.contrib.auth.decorators import login_required

# Create your views here.
@api_view(['POST'])
def SubmitExamen(request, exam_id):
    user=request.user
    if not user.is_stuff :
        return redirect('access_denied_student')
    exam = get_object_or_404(Exam, id=exam_id)
    if request.method == 'POST':
        exam.title = request.data
       
        return Response({
            "exam_id": exam_id,
            })
    return Response({
            
            "exam_id": exam_id,
            
            })
