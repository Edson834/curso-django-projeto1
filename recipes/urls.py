from django.urls import path
from recipes.views import home, sobre, contacto


urlpatterns = [
    path('', home), #Home
    path('sobre/', sobre), #Sobre
    path('contacto/', contacto), #Contacto
]