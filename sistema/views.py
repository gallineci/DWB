# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render

class Login(View): 


    def get(self, request):
            contexto = {'mensagem' : 'Sistema de cadastro de veiculos' }
            return render(request, "autenticacao.html",contexto)