from django.shortcuts import render
from .forms import VoitureForm
from . import models
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    if request.method == "POST":
        form = VoitureForm(request)
        if form.is_valid():
            Voiture = form.save()
            return render(request, "garage/affiche.html",{"Voiture" : Voiture})
        else:
            return render(request, "garage/index.html", {"form": form})
    else :
        form = VoitureForm()
        return render(request, "garage/index.html",{"form" : form})

def traitement(request):
    lform = VoitureForm(request.POST)
    if lform.is_valid():
        Voiture = lform.save()
        return render(request,"garage/affiche.html",{"Voiture" : Voiture})
    else:
        return render(request,"garage/index.html",{"form": lform})

def read(request, id):
    Voiture = models.Voiture.modele.get(pk=id)
    return render(request,"garage/affiche.html",{"Voiture": Voiture})

def update(request, id):
    lform = VoitureForm()


def traitementupdate(request, id):
    lform = VoitureForm(request.POST)
    if lform.is_valid():
        Voiture = lform.save(commit=False)
        Voiture.id = id;
        Voiture.save()
        return HttpResponseRedirect("/garage/")
    else:
        return render(request, "garage/update.html", {"form": lform, "id": id})