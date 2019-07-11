
from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    url(r'^create', views.create),
    url(r'^update$', views.update),
    url(r'^delete$', views.delete),
    url(r'^list$', views.list),
]
