# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
# myapp/views.py
from django.shortcuts import render

def code_view(request):
    # Example context data demonstrating DTL features
    context = {
        'title': 'Django Template Language Demo',
        'user': {
            'name': 'Alice',
            'age': 28,
            'is_active': True,
            'hobbies': ['Reading', 'Cycling', 'Programming'],
        },
        'items': ['apple', 'banana', 'cherry'],
        'number': 42,
        'price': 19.99,
        'html_string': '<b>This will be escaped</b>',
        'safe_html_string': '<b>This will NOT be escaped</b>',
        'nested_list': [
            {'name': 'John', 'score': 90},
            {'name': 'Jane', 'score': 85},
        ],
    }
    return render(request, 'code.html', context)
