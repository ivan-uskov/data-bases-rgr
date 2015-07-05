from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^detail/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]