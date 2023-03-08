from django.test import TestCase
from .models import Pets, Heroes
import os
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_adoption.settings'
class PetModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Pets.objects.create(name='Fluffy', species='dog', breed='Poodle', gender='female', color='white', age=3, spayed_neutered='Yes', is_available=True, vaccinated=True, poster='https://example.com/image.png')

    def test_pet_name_label(self):
        pet = Pets.objects.get(id=1)
        field_label = pet._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_pet_is_available_label(self):
        pet = Pets.objects.get(id=1)
        field_label = pet._meta.get_field('is_available').verbose_name
        self.assertEqual(field_label, 'is available')

    def test_heroes_weight_max_value(self):
        hero = Heroes.objects.create(name='Superman', species='dog', breed='Golden Retriever', gender='male', color='yellow', age=2, spayed_neutered='Yes', is_available=True, vaccinated=True, poster='https://example.com/image.png', personality='brave', job_title='superhero', favorite_food='steak', weight=20)
        self.assertRaisesMessage(ValueError, 'Ensure this value is less than or equal to 19.', hero.full_clean)


