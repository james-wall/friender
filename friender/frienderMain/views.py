from django.shortcuts import render

from django.http import HttpResponse
from frienderMain.models import User


def index(request):
	user_list = User.objects.order_by('-creationDate')[:5]
	context = {'user_list': user_list}
	return render(request, 'frienderMain/index.html', context)

def frienderButton(request, email):
	return HttpResponse("Hello, world. You're at the friender button")