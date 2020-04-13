from django.urls import path
from django.conf.urls import url
from .views import home, cri_status
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^cri/status$', cri_status, name='cri_status'),
]
