from django.http import HttpResponse

def index(request):
	return HttpResponse("<h6>Hello, world!<h6>")
