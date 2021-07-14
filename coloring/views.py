from django.shortcuts import render

def demo(request):
    return render(request, 'coloring/demo.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def homepage(request):
    return render(request, 'coloring/homepage.html')

def settings(request):
    return render(request, 'coloring/settings.html')

def help(request):
    return render(request, 'coloring/help.html')
