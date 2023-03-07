from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pets/', views.pets_list, name='pets_list'),
    path('pets/<int:pk>', views.PetDetails.as_view(), name='pets_details'),
    path('heroes/', views.pets_heroes, name='pets_heroes'),
    #path('heroes/', views.pets_heroes, name='pets_heroes'),
    path('pets/delete/<int:pk>', views.PetDelete.as_view(), name='pets_delete'),
    path('heroes_in_action', views.heroes_in_action, name = 'heroes_in_action'),
    path('pets/add', views.PetCreate.as_view(), name='pets_create'),
    path('heroes/add', views.HeroesCreate.as_view(), name='heroes_create'),
    path('pets/update/<int:pk>', views.PetUpdate.as_view(), name='pets_update'),
    path('heroes/update/<int:pk>', views.HeroesUpdate.as_view(), name='heroes_update'),
    path('heroes/<int:pk>', views.HeroesDetails.as_view(), name='heroes_details'),
    path('heroes/delete/<int:pk>', views.HeroesDelete.as_view(), name='heroes_delete'),
   # path('adopt_pets', views.adopt_pets, name = 'adopt-pets'),
]
