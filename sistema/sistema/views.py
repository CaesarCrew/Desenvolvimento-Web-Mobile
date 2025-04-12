from django.shortcuts import render
from django.views import View

class Login(View):
    def get(self, request):
        contexto = {'mensagem': 'Sistema de cadastro de veículo'}
        return render(request, 'autenticacao.html', contexto)