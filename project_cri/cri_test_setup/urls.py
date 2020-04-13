from django.urls import path
from django.conf.urls import url
from .views import home, cri_test_setup_status
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^cri_test_setup/status$', cri_test_setup_status, name='cri_test_setup_status'),
]
