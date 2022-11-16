
from django.shortcuts import redirect, render
from app.forms import PersonForm
from app.models import Person

def home (request):
    return render(request,'index.html')

def lista (request):
    data ={}
    data['bd'] = Person.objects.all()
    return render(request,'lista.html',data)

## coleta os dados do tempeite de forms.
def form (request):
    data={}
    data['form'] = PersonForm()
    return render(request,'forms.html',data)

## insere os datos vindo do templeite de forms, na tabela do banco
def create(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view (request,pk):
    data ={}
    data['db'] = Person.objects.get(pk=pk)
    return render(request,'view.html',data)

def edit(request,pk):
    data = {}
    data['bd'] = Person.objects.get(pk=pk)
    data['form'] = PersonForm(instance=data['bd'])
    return render(request,'forms.html',data)

def update (request,pk):
    data = {}
    data['db'] = Person.objects.get(pk=pk)
    form = PersonForm(request.POST or None,instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')