from django.shortcuts import render
from .models import Familiar

def index(request):

    familia = Familiar.objects.all()

    ctx = {'parientes':familia,}

    return render(request, 'familia/index.html', ctx)
