from django.urls import path
from .views import AppointmentView, AppointProba

urlpatterns = [
    path('appointment/make_appointment/', AppointmentView.as_view(), name='make_appointment'),
    #path('appointment/make_appointment/', AppointProba.as_view(), name='make_appointment'),

]
