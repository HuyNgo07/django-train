from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1> Welcome to Little Lemon! </h1>")


def drinks(request, drink_name):
    drink_items={
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment',
    }
    choice_of_drink = drink_items[drink_name]
    return HttpResponse(f"<h2> {drink_name} </h2> <p> {choice_of_drink} </p>")

def about(request):
    return HttpResponse("<h1> About </h1>")


def book(request):
    return HttpResponse("<h1> Book </h1>")


def menu(request):
    return HttpResponse("<h1> Menu </h1>")