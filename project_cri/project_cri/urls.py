"""project_cri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from cri import views as criview

admin.site.site_header = 'CRI administration'
#admin.site.site_title = 'CRI administration'
#admin.site.index_title = 'CRI administration'
#https://www.google.com/search?q=change+Django+administration+title&oq=change+Django+administration+title&aqs=chrome..69i57.9159j0j1&sourceid=chrome&ie=UTF-8#kpvalbx=_psiOXpvWMfPez7sP7q2lgA056

urlpatterns = [
    path('', include('cri.urls')),
    path('', include('cri_test_setup.urls')),
    #url(r'^$', criview.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

]
