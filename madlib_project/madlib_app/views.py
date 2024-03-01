from django.shortcuts import render, redirect
from .forms import MadLibForm
from .models import Madlib
from django.template import loader
import random


def madlib_form(request):
    if request.method == 'POST':
        form = MadLibForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('madlib_result')
    else:
        form = MadLibForm()
    return render(request, 'madlib_app/madlib_form.html', {'form': form})


def madlib_result(request):
    madlib = Madlib.objects.last()
    if madlib is None:
        return render(request, 'madlib_app/madlib_template_1.html')
    template_number = random.randint(1, 15)
    template_name = f'madlib_app/madlib_template_{template_number}.html'
    madlib_story = generate_madlib(madlib, template_name)
    return render(request, 'madlib_result.html', {'madlib_story': madlib_story})


def submit_madlib(request):
    if request.method == 'POST':
        form = MadLibForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('madlib_result')
    return render(request, 'madlib_app/madlib_result.html', {'form': form})


def generate_madlib(madlib_instance, template_name):
    context = {
        'name': madlib_instance.name,
        'verb': madlib_instance.verb,
        'time': madlib_instance.time,
        'noun': madlib_instance.noun,
        'pronoun': madlib_instance.pronoun,
        'adjective': madlib_instance.adjective,
        'place': madlib_instance.place,
    }

    madlib_story = render(None, template_name, context).content.decode('utf-8')

    return madlib_story
