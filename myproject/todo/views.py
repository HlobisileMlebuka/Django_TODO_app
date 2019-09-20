from django.shortcuts import render
from .models import ToDo
from .forms import ToDoForm

def index(request):
    todo_list = ToDo.objects.order_by('id')

    form = ToDoForm()

    context = {'todo_list' : todo_list, 'form': form} 
    return render(request,'todo/index.html', context)
