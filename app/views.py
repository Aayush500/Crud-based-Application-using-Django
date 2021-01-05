from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .forms import UserForm
from .models import User

# Create your views here.
def save_data(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        form = UserForm()
    
    else:
        form = UserForm()
    users = User.objects.all()
    params = {'forms': form, 'users': users}
    return render(request, 'Home.html', params)


def edit(request, my_id):
    if request.method == 'POST':
        user = User.objects.get(id=my_id)
        form = UserForm(request.POST, instance= user)
        if form.is_valid():
            form.save()
            return render(request, 'Edit.html', {'updated': True})
    
    else:
        user = User.objects.get(id = my_id)
        form = UserForm(instance=user)
    return render(request, 'Edit.html', {'forms': form, 'my_id': my_id})


def delete(request, delete_id):
    if request.method == 'POST':
        user = User.objects.get(pk= delete_id)
        user.delete()
    return HttpResponseRedirect('/')