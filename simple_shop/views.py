from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'user': request.session.get('user')})