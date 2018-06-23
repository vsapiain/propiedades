from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import Context, loader

# Create your views here.
def index(request):
    t = loader.get_template('index.html')
    context = {'list_var': ''}
    return HttpResponse(t.render(context))

def propiedades(request):
    t = loader.get_template('propiedades.html')
    context = {'list_var': ''}
    if request.method == "POST":
        pass
    return HttpResponse(t.render(context))
