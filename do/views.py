from django.shortcuts import render,redirect
from .models import Do
# Create your views here.

def index(request):
    do = Do.objects.all()
    if request.method == 'POST':
        new_todo = Do(
            title=request.POST['title']
        )
        new_todo.save()
        return redirect('/')

    return render(request, 'index.html', {'do': do})


def delete(request, pk):
    do = Do.objects.get(id=pk)
    do.delete()
    return redirect('/')
