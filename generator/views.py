from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')
def password(request):

    cheracter = list('abcdefgijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        cheracter.extend(list('ABCDEFGIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        cheracter.extend(list('@#%$^&*()+='))

    if request.GET.get('numbers'):
        cheracter.extend(list('0123456789'))
    length = int(request.GET.get('length',12))
    thepassword = ''

    for x in  range(length):
        thepassword += random.choice(cheracter)

    return render(request,'generator/password.html', {'password':thepassword })