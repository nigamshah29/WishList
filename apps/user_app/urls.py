from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name="login"),
    url(r'^authenticate$', authenticate, name="authenticate"),
    url(r'^register$', register, name="register"),
    url(r'^logout$', logout, name="logout")
]
