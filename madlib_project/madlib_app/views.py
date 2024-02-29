from django.shortcuts import render, redirect
from .forms import MadLibForm
from .models import Madlib


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
    return render(request, 'madlib_result.html', {'madlib': madlib})


def submit_madlib(request):
    if request.method == 'POST':
        form = MadLibForm(request.POST or None)
        if form.is_valid():
            madlib = form.save()
            madlib_pk = madlib.pk
            return redirect('result/', pk=madlib_pk)
    return render(request, 'madlib_app/madlib_result.html', {'form': form})
