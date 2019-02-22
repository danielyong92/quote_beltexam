#URLS FOR LOGIN APP

from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^processing$', views.processing),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^clear$', views.clear), # logout and clear sessions
]