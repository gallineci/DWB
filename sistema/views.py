# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render

class Login(View): 


    def get(self, request):
        contexto = {'mensagem' : ''}
        if request.user.is_authenticated:
            return redirect ("/veiculo")
        else:
            return render (request, 'autentificacao.html', contexto)
        """
            contexto = {'mensagem' : 'Sistema de cadastro de veiculos' }
            return render(request, "autenticacao.html",contexto)
        """