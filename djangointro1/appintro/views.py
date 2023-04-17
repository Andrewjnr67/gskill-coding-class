from django.shortcuts import render


 
# Create your views here.
def index(request):
    page = 'landing page'
    age = 22
    context = {
        'msg': page,
        'years_old': age
    }
    return render(request, 'appintro/index.html', context)

def about(request):
    page: 'About us page'
    return render(request, 'appintro/about.html', {'msg': page})
