from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todoItems

# Create your views here.

def home(request):
    all_todo_items = todoItems.objects.all()

    return render(request, 'todoApp/home.html',
            {'all_items': all_todo_items})


def addTodo(request):
    content = request.POST['content']
    new_content = todoItems(content = content)
    new_content.save()

    return HttpResponseRedirect('/todoApp/')

def deleteTodo(request, todo_id):
    item_to_delete = todoItems.objects.get(id = todo_id)
    item_to_delete.delete()
    
    return HttpResponseRedirect('/todoApp/')

