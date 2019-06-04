from django.http import HttpResponse

def index(request):
	return HttpResponse("<p>Hola</p> <h1>Hello, world!</h1>")
