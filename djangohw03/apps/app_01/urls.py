from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index ,name="index"),
    url(r'^random_word/$', views.random_word ,name="random_word"),
    url(r'^random_word/reset$', views.reset ,name="reset")
]