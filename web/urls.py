from django.urls import path
from web import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("products/travelslowlife", views.travelslowlife, name="travelslowlife"),
    path("faq", views.faq, name="faq"),
    path("tandc", views.tandc, name="tandc"),
    path("privacy", views.privacy, name="privacy"),
    path("products/bidjourney", views.bidjourney, name="bidjourney"),
    path("products/dropdata", views.dropdata, name="dropdata"),
    path("products/tripkart", views.tripkart, name="tripkart"),
    path("send_email", views.send_email, name="send_email"),
    path("subscribe", views.subscribe, name="subscribe"),
]