from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def your_django_endpoint(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        my_var = data.get('input')
        # Делайте что-то с переменной myVar
        return JsonResponse({'message': 'Данные успешно получены и обработаны'})
    else:
        return JsonResponse({'error': 'Метод не разрешен'}, status=405)
