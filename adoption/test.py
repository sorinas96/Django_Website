from django.test import TestCase, Client
from django.urls import reverse
from .models import Pets

class PetsAdoptionPageTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.pet1 = Pets.objects.create(name='Snow', species='dog', breed='Husky', age=1, gender='F')
        self.pet2 = Pets.objects.create(name='Snow', species='dog', breed='Husky', age=1, gender='F')
        self.pet3 = Pets.objects.create(name='Snow', species='dog', breed='Husky', age=1, gender='F')
        self.pets_list_url = reverse('pets_list')
        self.pet_details_url = reverse('pet_details', kwargs={'pet_id': self.pet1.id})

    def test_pets_list_view(self):
        response = self.client.get(self.pets_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pets_list.html')
        self.assertContains(response, 'Fluffy')
        self.assertContains(response, 'Max')
        self.assertContains(response, 'Whiskers')

    def test_pet_details_view(self):
        response = self.client.get(self.pet_details_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pet_details.html')
        self.assertContains(response, 'Fluffy')
        self.assertContains(response, 'Persian')
        self.assertContains(response, '2')
        self.assertContains(response, 'F')
        self.assertContains(response, 'S')

    def test_add_pet_view(self):
        new_pet_data = {'name': 'Buddy', 'species': 'dog', 'breed': 'Golden Retriever', 'age': 2, 'gender': 'M', 'size': 'L'}
        response = self.client.post(reverse('add_pet'), data=new_pet_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Pets.objects.count(), 4)
        self.assertTrue(Pets.objects.filter(name='Buddy').exists())

    def test_heroes_in_action_view(self):
        response = self.client.get(reverse('heroes_in_action'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'heroes_in_action.html')
        self.assertContains(response, 'Fluffy')
        self.assertContains(response, 'Max')
        self.assertContains(response, 'Whiskers')
        self.assertNotContains(response, 'Buddy')