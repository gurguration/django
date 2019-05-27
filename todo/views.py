from django.shortcuts import render, redirect
from .models import Todo
from django.views.decorators.http import require_POST
from .forms import MyForm
#from django.http import HttpResponse
# Create your views here.

def index(request):
    form = MyForm()
    todo_list = Todo.objects.order_by('id')
    context = {
            'todo_list': todo_list,
            'form': form
            }
    return render(request, 'todo/index.html', context)

def complete(request, id):
    done = Todo.objects.get(pk=id)
    done.completed = True
    done.save()
    return redirect('todo:index')

@require_POST
def add(request):
    print(request.POST)
    myform = MyForm(request.POST)
    if myform.is_valid():
        new_todo = Todo(text=myform.cleaned_data['text'])
        new_todo.save()
    return redirect('todo:index')

def deleteComplete(request):
    Todo.objects.filter(completed__exact=True).delete()
    print('delete completed')
    return redirect('todo:index')

def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('todo:index')
