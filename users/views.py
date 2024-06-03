from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.models import User
import json

@csrf_exempt  # Disable CSRF for this view
def receive_user_data(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        username = data.get('name')
        email = data.get('email')

        print(username)
        print(email)

        new_user = User.objects.create_user(
            username=username,
            email=email
        )

        new_user.save()

        return JsonResponse({'status': 'success', 'data': data})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)

