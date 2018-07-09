from django.shortcuts import render
from .models import Users
from django.utils import timezone

def login(request):
    return render(request, '/home/ali/talent-finder/TF/Finder/templates/w.html')

def authentication(request):
	name=request.GET.get('uname',default=None)
	password=request.GET.get('psw',default=None)
	print(name,password)
	latest_users_list = Users.objects.order_by('-created_date')
	print(latest_users_list[0].username)
	for x in latest_users_list:
		if x.username==name and x.password==password:
			return render(request, '/home/ali/talent-finder/TF/Finder/templates/signup.html')
		else:
			return render(request, '/home/ali/talent-finder/TF/Finder/templates/w.html')

def signup(request):
	return render(request, '/home/ali/talent-finder/TF/Finder/templates/signup.html')

def signup_new_user(request):
	name=request.GET.get('uname',default=None)
	password=request.GET.get('psw',default=None)
	new_user=Users(username=name , password=password,Email="",created_date=timezone.now())
	print(name,password)
	new_user.save()
	print(Users.objects.all())
	return render(request, '/home/ali/talent-finder/TF/Finder/templates/signup.html')
