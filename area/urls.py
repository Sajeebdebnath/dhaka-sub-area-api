from django.urls import path

from area.views import DhakaArea

urlpatterns = [
    path('', DhakaArea, name='home'),

]
