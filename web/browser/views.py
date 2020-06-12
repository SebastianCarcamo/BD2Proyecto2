from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import Context, loader

# Create your views here.

def index(request):
	template = loader.get_template("index.html")
	return HttpResponse(template.render())


@require_http_methods(["POST"])
def search(request):
	tweets = ['1271515272575430656', '1271496282016751617']
	return JsonResponse({'tweets': tweets})
