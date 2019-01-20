from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.main),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    # url(r'^reset$', views.reset),
]
