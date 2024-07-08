from django.shortcuts import render
from musician.models import MusicianModel

def home(request):
    data = MusicianModel.objects.all()
    return render(request, 'index.html', {'data': data})
