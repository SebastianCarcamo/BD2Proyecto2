from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import Context, loader
from files.utils import get_n_most_similar

# Create your views here.

def index(request):
	template = loader.get_template("index.html")
	return HttpResponse(template.render())


@require_http_methods(["POST"])
def search(request):
	search_terms = request.POST.get('searchTerms')
	tweets = get_n_most_similar(search_terms, 10)
	return JsonResponse({'tweets': [x[1] for x in tweets]})
