from django.urls import path

from area.views import CityList, dhakaArea, dhakaArea_details

urlpatterns = [
    path('', dhakaArea),
    path('list', CityList.as_view()),
    path('<name>', dhakaArea_details),

]
