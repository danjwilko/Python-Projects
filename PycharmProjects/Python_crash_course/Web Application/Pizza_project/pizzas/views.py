from django.shortcuts import render

from .models import Pizza

def index(request):
    """ The home page for Pizza app"""
    return render(request, 'pizzas/index.html')

def pizza(request):
    """ Show all pizzas """
    pizza = Pizza.objects.all()
    context = {'pizzas': pizza}
    return render(request, 'pizzas/pizza.html', context)

def toppings(request, pizza_id):
    """ Show pizza details """
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza_toppings.html', context)