from django.conf.urls import url
from . import views

app_name = 'recipes'

urlpatterns = [
    url(r'^$', views.recipes, name='recipes'),
]