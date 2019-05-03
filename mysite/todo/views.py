from django.shortcuts import render,redirect,get_object_or_404



from .models import Zadacha
from .forms import PostForm

# Create your views here.
def post_list(request):
	n = Zadacha.objects.all()
	return render(request, 'todo/index.html', context={'Zadacha': n})


def quote_list(request):
	p = Quote.objects.all()
	return render(request, 'todo/index.html', context={'Chytata': p})
def post_detail(request, pk):
	post = get_object_or_404(Zadacha, pk=pk)
	return render(request, 'todo/post_detail.html', {'post': post})


def post_edit(request, pk):
	post = get_object_or_404(Zadacha, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.save()
			return redirect('post_detail', pk=todo.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'todo/post_edit.html', {'form': form})
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.save()
			return redirect('post_detail', pk=todo.pk)
	else:
		form = PostForm()
	return render(request, 'todo/post_edit.html', {'form': form})