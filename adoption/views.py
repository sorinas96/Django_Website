from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404
from .models import Pets
from .models import Heroes
def index(request):
    return HttpResponse("Hello, world. You're at the adoption app index.")

def pets_list(request):
    #luam toate animalele din db
    try:
        pets = Pets.objects.all()
    except Pets.DoesNotExist:
        raise Http404 (f"There are no pets in our Data Base!")
    else:
        return render(request, 'adoption/pets_list.html', {"pets": pets})

def pets_heroes(request):
    #luam toate animalele din db
    try:
        heroes = Heroes.objects.all()
    except Heroes.DoesNotExist:
        raise Http404 (f"There are no pets in our Data Base!")
    else:
        return render(request, 'adoption/pets_heroes.html', {"heroes": heroes})

#def adopt_pets(request):
  #  return render (request, "adoption/adopt_pets.html", {})

class PetDetails(generic.DetailView):
    model = Pets
    template_name = "adoption/pets_details.html"
    #context_object_name = "pet"

class HeroesDetails(generic.DetailView):
    model = Heroes
    template_name = "adoption/heroes_details.html"
    #context_object_name = "pet"

class HeroesDelete(generic.DeleteView):
    model = Heroes
    template_name = "adoption/confirm_delete.html"
    context_object_name = "heroes"
    success_url = "/adoption/heroes#projects"
#DELETE PET
class PetDelete(generic.DeleteView):
    model = Pets
    template_name = "adoption/confirm_delete.html"
    context_object_name = "pets"
    success_url = reverse_lazy("pets_list")

#UPDATE PET
class PetUpdate(generic.UpdateView):
    model = Pets
    template_name = "adoption/pets_form.html"
    fields=['name','breed','gender','color','age','poster']
    context_object_name = "pets"
    success_url = reverse_lazy("pets_list")



 # ADD PET
class PetCreate(generic.CreateView):
    model = Pets
    template_name = "adoption/pets_form.html"
    fields = ['name', 'species','breed', 'gender', 'color', 'age','spayed_neutered','is_available','vaccinated', 'poster']
    context_object_name = "pets"
    success_url = reverse_lazy("pets_list")

 # ADD Hero
class HeroesCreate(generic.CreateView):
    model = Heroes
    template_name = "adoption/heroes_form.html"
    fields = ['name', 'weight','species','breed', 'gender', 'color', 'age','spayed_neutered','is_available','vaccinated', 'poster']
    context_object_name = "heroes"
    success_url = "/adoption/heroes#projects"


def heroes_in_action(request):
    return render(request, 'adoption/heroes_in_action.html')