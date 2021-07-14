from django.shortcuts import render

def index(request):
    return render(request, 'coloring/homepage.html')

def demo(request):
    return render(request, 'coloring/homepage.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def homepage(request):
    return render(request, 'coloring/homepage.html')

def settings(request):
    return render(request, 'coloring/settings.html')
