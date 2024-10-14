from django.shortcuts import render
from django.http import JsonResponse
import random

def index(request):
    return render(request, 'generator/index.html')

def generate_number(request):
    min_value = int(request.GET.get('min'))
    max_value = int(request.GET.get('max'))
    random_number = random.randint(min_value, max_value)
    return JsonResponse({'number': random_number})
