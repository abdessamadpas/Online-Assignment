from django import forms
from core.models.student import Student

class StudentForm(forms.ModelForm):

	class Meta:

		model = Student
		fields = ('name', 'email', 'group_id')