
from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # Sets up the url for the about page.
    url(r'^about/', views.about, name='about'),

]
