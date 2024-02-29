from django.shortcuts import render, redirect
from .forms import MadLibForm
from .models import Madlib
from django.template import loader

def madlib_form(request):
    if request.method == 'POST':
        form = MadLibForm(request.POST or None)
        if form.is_valid():
            madlib = form.save()
            return redirect('madlib_result', pk=madlib.pk)
    else:
        form = MadLibForm()
    return render(request, 'madlib_form.html', {'form': form})


def madlib_result(request, pk):
    madlib = Madlib.objects.get(pk=pk)
    madlib_story = generate_madlib(madlib)
    return render(request, 'madlib_result.html', {'madlib_story': madlib_story})


def submit_madlib(request):
    if request.method == 'POST':
        form = MadLibForm(request.POST or None)
        if form.is_valid():
            madlib = form.save()
            madlib_pk = madlib.pk
            return redirect('madlib_result', pk=madlib_pk)
    return render(request, 'madlib_app/madlib_result.html', {'form': form})


def generate_madlib(madlib_instance):
    context = {
        'name': madlib_instance.name,
        'verb': madlib_instance.verb,
        'time': madlib_instance.time,
        'noun': madlib_instance.noun,
        'pronoun': madlib_instance.pronoun,
        'adjective': madlib_instance.adjective,
        'place': madlib_instance.place,
    }

    madlib_story = render(None,f'madlib_app/{madlib_instance.template_name}', context)

    return madlib_story
