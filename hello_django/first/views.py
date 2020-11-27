from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from random import sample


def show_index(request):
    return HttpResponse('<h1>Hello, Django!</h1>')


def show_fruit(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = sample(fruits, 3)
    content = '<h3>今天推荐的水果是：</h3>'
    content += '<hr>'
    content += '<ul>'
    for fruit in selected_fruits:
        content += f'<li>{fruit}</li>'
    content += '</ul>'
    return HttpResponse(content)


def show_fruit_2(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry',
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = sample(fruits, 3)
    return render(request, 'fruit.html', {'fruits': selected_fruits})

