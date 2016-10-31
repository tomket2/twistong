from django.shortcuts import render
from .models import Twister

# Create your views here.
def index(request):
    twister_list = Twister.objects.all()
    return render(request, 'index.html', {'twister':twister_list})

def detail(request, twister_id):
    twister_list = Twister.objects.get(id=twister_id)
    return render(request, 'detail.html', {'twister':twister_list})
