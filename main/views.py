from django.shortcuts import render

# Create your views here.

def index(request):
  if request.POST:
    context = {
      'name': request.POST['name'],
      'email': request.POST['email'],
    }
    return render(request, 'thanks.html', context)
  context = {
    'results': [
      {'name': 'Fatima Lopez', 'email': 'f.lopez@gmail.com'},
      {'name': 'Gary Johnston', 'email': 'g.johnston@gmail.com'},
      {'name': 'Jeyna Kim', 'email': 'jeyna.kim@gmail.com'},
      {'name': 'Arnel Robbin', 'email': 'arnel.robbin@gmail.com'}
    ]
  }
  return render(request, 'index.html', context)
