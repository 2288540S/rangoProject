
from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # Sets up the url for the about page.
    url(r'^about/', views.about, name='about'),
    # Sets up the url for the category page.
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),

]
