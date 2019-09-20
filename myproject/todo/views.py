from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm
from django.views.decorators.http import require_POST

def index(request):
    todo_list = ToDo.objects.order_by('id')

    form = ToDoForm()

    context = {'todo_list' : todo_list, 'form': form} 
    return render(request,'todo/index.html', context)

@require_POST
def add_todo(request):
    '''takes in the form data, that is instantiated with the form data'''

    form = ToDoForm(request.POST)
    print(request.POST['text'])
    
    #save form data to database
    if form.is_valid():
        new_todo = ToDo(text=request.POST['text'])
        new_todo.save()
    
    #redirected back to the index
    return redirect('index')

def complete_todo(request, todo_id):

    todo = ToDo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def delete_completed(request):
    #search database for completed todos
    ToDo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def delete_all(request):
    ToDo.objects.all().delete()

    return redirect('index')
