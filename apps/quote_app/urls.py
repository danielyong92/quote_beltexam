#URL FOR BELT EXAM
from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^quotes$', views.quote),
    url(r'^add_quote$', views.addquote),
    url(r'^user/(?P<id>\d+)$', views.userquotes),
    url(r'^myaccount/(?P<id>\d+)$', views.account),
    url(r'^edit/(?P<id>\d+)$', views.editaccount),
    url(r'^back$', views.back),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^like_message/(?P<id>\d+)$', views.like)
]