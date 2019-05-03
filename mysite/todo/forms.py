from django import forms
from .models import Zadacha

class PostForm(forms.ModelForm):

	class Meta: 
		model = Zadacha
		fields = ('Opisanie', 'status')