from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout
from django.views.generic import TemplateView




class IndexView(TemplateView):
	template_name = 'index.html'

def LogOut(request):
	logout(request)
	return redirect('/')

def jugad(request):
	return render_to_response("jugador.html")

def equip(request):
	return render_to_response("equipo.html")

def inde(request):
	return render_to_response("index.html")

def campeonat(request):
	return render_to_response("campeonato.html")



