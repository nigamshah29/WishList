from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^add_item_page$', add_item_page, name="add_item_page"),
    url(r'^add_item$', add_item, name="add_item"),
    url(r'^remove_item/(?P<item_id>\d+)/$', remove_item, name="remove_item"),
    url(r'^add_to_list/(?P<item_id>\d+)/(?P<adder_id>\d+)/$', add_to_list, name="add_to_list"),
    url(r'^wish_item/(?P<item_id>\d+)/$', wish_item, name="wish_item"),
]
