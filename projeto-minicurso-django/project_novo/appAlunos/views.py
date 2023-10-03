from django.shortcuts import redirect,render
from .models import Member

def index(request):
    mem=Member.objects.all()
    return render(request, 'index.html',{'mem':mem})

def add(request):
	return render(request,'add.html')

def addrec(request):
	x=request.POST['nome']
	y=request.POST['sobrenome']
	z=request.POST['curso']
	mem=Member(nome=x,sobrenome=y,curso=z)
	mem.save()
	return redirect("/")


def delete(request,id):
	mem=Member.objects.get(id=id)
	mem.delete()
	return redirect("/")

def update(request,id):
	mem=Member.objects.get(id=id)
	return render(request,'update.html',{'mem':mem})

def uprec(request,id):
	x=request.POST['nome']	
	y=request.POST['sobrenome']	
	z=request.POST['curso']	
	mem=Member.objects.get(id=id)
	mem.nome=x
	mem.sobrenome=y
	mem.curso=z
	mem.save()
	return redirect("/")

