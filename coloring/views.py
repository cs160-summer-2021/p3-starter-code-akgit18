from django.shortcuts import render
import os

def demo(request):
    return render(request, 'coloring/demo.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def homepage(request):
    context_dict = {}
    files = os.listdir(os.path.join("coloring/static/", "coloring/images"))
    context_dict['files'] = ['coloring/images/'+x for x in  files[0:]]
    return render(request, 'coloring/homepage.html', context=context_dict)

def settings(request):
    return render(request, 'coloring/settings.html')

def help(request):
    return render(request, 'coloring/help.html')
