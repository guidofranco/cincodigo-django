from django.http import HttpResponse

def index(request):
	return HttpResponse("<h4>Hello, word!</h4>")