from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from todoapp.models import Todo

# Create your views here.

def home(request):
    todo = Todo.objects.all().order_by("-fecha")
    contexto = {
        'todo': todo,
    }
    return render(request, 'index.html', contexto)

@csrf_protect
def add_todo(request):
    # print(request.POST)
    fecha_creada = timezone.now()
    contenido_creado = request.POST["contenido"]
    obj = Todo.objects.create(fecha = fecha_creada, texto = contenido_creado)
    # print(obj.id)
    length_todo = Todo.objects.all().count()
    print(length_todo)
    return redirect("/home/")

@csrf_protect
def delete_todo(request, it_id):
    # print(it_id)
    Todo.objects.get(id = it_id).delete()
    return redirect('/home/')
