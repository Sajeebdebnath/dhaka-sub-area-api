from django.urls import path

from area.views import dhakaArea, dhakaArea_details

urlpatterns = [
    path('', dhakaArea, name='all_city'),
    path('<name>', dhakaArea_details, name='details'),

]
