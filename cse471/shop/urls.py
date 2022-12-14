from django.urls import path
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("login/", views.Login, name="LogIn"),
    path("signup/", views.signup, name="SignUp"),
    path("logout/", views.Logout, name="Logout"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("search/", views.search, name="Search"),
    path("nomatch/", views.search,name="nomatch"),
    path("product/<int:id>", views.product, name="product"),
    path("checkout/", views.checkout, name="Checkout"),
    path("prescribed/", views.prescribed, name="prescribed"),
    path("otc/", views.otc, name="otc"),
    path("healthcare/", views.healthcare, name="healthcare"),
]
urlpatterns += staticfiles_urlpatterns()