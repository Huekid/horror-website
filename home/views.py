from django.shortcuts import render
from home.models import Contract
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        form_first_name = request.POST['name']
        form_initials = request.POST['initials']

        Contract.objects.create(fname=form_first_name, initial=form_initials)
        print(Contract.objects.all())

        return render(request, 'home/game.html')

    return render(request, 'home/home.html',)
