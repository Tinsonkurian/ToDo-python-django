from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    dict_todo = {
        'task': Todo.objects.all()
    }
    if request.method == 'POST':
        name = request.POST['name']
        priority = request.POST['priority']
        date = request.POST['date']
    
        task = Todo(
            name = name,
            priority = priority,
            date = date
        )
        
        task.save()
        print("inserted")
        return redirect('/')
    return render(request, 'index.html', dict_todo)

def delete(request,id):
    dict_task = {
        'task' : Todo.objects.get(id=id)
    }
    if request.method == 'POST':
        deletetask = Todo.objects.get(id = id)
        deletetask.delete()
        return redirect('/')
    

    return render(request, 'delete.html', dict_task)

def edit(request, id):
    dict_task = {
        'task' : Todo.objects.get(id=id)
    }
    print(dict_task)
    return render(request, 'update.html', dict_task)

def update(request,id):
    
    if request.method == 'POST':
        name = request.POST['name']
        priority = request.POST['priority']
        date= request.POST['date']

        todo = Todo.objects.get(id=id)
        todo.name = name
        todo.priority = priority
        todo.date = date

        todo.save()
        return redirect('/')

