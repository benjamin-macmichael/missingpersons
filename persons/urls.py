from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import actPageView
from .views import contactPageView
            
urlpatterns = [
    path("about/", aboutPageView, name="about"),
    path("act/", actPageView, name="act"),
    path("contact/", contactPageView, name="contact"),
    path("", indexPageView, name="index")    
]  