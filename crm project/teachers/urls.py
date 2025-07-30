from . import views
from django.urls import path
urlpatterns = [
    path('',views.lan,name="hello"),
    path('add/',views.add,name="ss"),
    path("up/<str:id>",views.update,name="oo"),
    path("fhd/<str:id>",views.dle,name="delte"),
]