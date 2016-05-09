from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import RequestContext

# Create your views here.
def index(request):
    return render(request, 'soccermarket.html')

# def search(request):
#     if request.method == 'POST':
#         text = request.POST['search']
#         users = Usuario.objects.filter(username__contains=text)
#         questoes = Questao.objects.filter(nome__contains=text)
#         for i in questoes:
#             i.nome = i.nome.strip()
#         return render(request, 'search/search.html', { 'users' : users , 'questoes' : questoes[:100] })
#     return redirect(reverse('index'))
