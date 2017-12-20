from . import views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns


app_name = "products"

urlpatterns = [
    url(r'^$', views.product_list, name='home'),
    url(r'^menclothes/$', views.menclothes, name="menclothes"),
    url(r'^menshoes/$', views.menshoes, name="menshoes"),
    url(r'^womenclothes/$', views.womenclothes, name="womenclothes"),
    url(r'^womenshoes/$', views.womenshoes, name="womenshoes"),
    url(r'^shoppingcart/$', views.shoppingcart, name="shoppingcart"),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    url(r'^checkout/$', views.checkout, name="checkout"),
    url(r'^checkoutnext/$', views.checkoutnext, name="checkoutnext"),
    url(r'^price_filter/$', views.price_filter_product_list, name="price_filter_product_list"),
    url(r'^price_filter_men_clothes/$', views.price_filter__men_clothes, name="price_filter__men_clothes"),
    url(r'^price_filter_men_shoes/$', views.price_filter_men_shoes, name="price_filter_men_shoes"),
    url(r'^price_filter_woman_clothes/$', views.price_filter_woman_clothes, name="price_filter_woman_clothes"),
    url(r'^price_filter_woman_shoes/$', views.price_filter_woman_shoes, name="price_filter_woman_shoes"),
    url(r'^api_product/$', views.ProductList.as_view()),
    url(r'^api_product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^api_user/$', views.UserList.as_view()),
    url(r'^api_user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
