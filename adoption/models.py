from django.db import models
from django.core.validators import MaxValueValidator

spayed_neutered= [('Yes', 'Yes'),('No', 'No')]
pet_species = [('Dog', 'Dog'),('Cat', 'Cat')]

# Create your models here.
class Pets(models.Model):
    name = models.CharField(max_length=200, default='')  # new field
    species = models.CharField(max_length=5, choices=pet_species)
    breed = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    age = models.IntegerField(validators=[MaxValueValidator(19)])
    spayed_neutered = models.CharField(max_length=5, choices=spayed_neutered, default='Yes')
    is_available = models.BooleanField(default=True)
    vaccinated = models.BooleanField(default=True)
    poster = models.CharField(max_length= 1000, null= True, blank= True, default=None )

    def __str__(self):
        return f"Pets(breed ={self.breed}, gender ={self.gender} name ={self.name}, color ={self.color}, age ={self.age}, spayed_neutered ={self.spayed_neutered},is_available ={self.is_available}, vaccinated ={self.vaccinated})"

    def __repr__(self):
        return self.__str__()

class Heroes(Pets):

    personality = models.CharField(max_length=200, default='')
    job_title = models.CharField(max_length=200, default='')
    favorite_food = models.CharField(max_length=200, default='')
    weight = models.IntegerField(validators=[MaxValueValidator(19)])


    def __str__(self):
        return f"Heroes(name ={self.name}, personality ={self.personality},job_title ={self.job_title},favorite_food ={self.favorite_food},breed ={self.breed},gender ={self.gender},color ={self.color},age ={self.age},weight ={self.weight})"

    def __repr__(self):
        return self.__str__()



