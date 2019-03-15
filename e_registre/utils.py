from django.contrib.auth.models import User

def get_current_user(request):
	if request.user.is_authenticated:
		return request.user
	else:
		return User.objects.filter(username='guest')[0]