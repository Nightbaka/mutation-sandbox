from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.models import User
import json

@csrf_exempt
def receive_login_data(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        email = data.get('email')

        try:
            user = User.objects.get(email=email)
            return JsonResponse({'status': 'success', 'data': {'username': user.username, 'email': user.email}})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User not found. Register for access.'}, status=404)

    return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def receive_registration_data(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        username = data.get('name')
        email = data.get('email')

        if not User.objects.filter(email=email).exists():

            new_user = User.objects.create_user(
                username=username,
                email=email
            )

            new_user.save()

            return JsonResponse({'status': 'User registered successfully', 'data': data})
        else:
            return JsonResponse({'status': 'error', 'message': 'This user is already registered. Try logging in instead'}, status=405)

    return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)