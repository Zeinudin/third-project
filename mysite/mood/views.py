from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Diary
from django.urls import reverse_lazy

class DiaryList(ListView):
	model = Diary

class DiaryDetail(DetailView):
	model = Diary

class DiaryCreate(CreateView):
	model = Diary
	fields = ['text', 'scale', 'do_exercises']
	success_url = reverse_lazy('diary_list')

class DiaryUpdate(UpdateView):
	model = Diary
	fields = ['text', 'scale', 'time_now']
	success_url = reverse_lazy('diary_list')

class DearyDelete(DeleteView):
	model = Diary
	success_url = reverse_lazy('diary_list')