from django.shortcuts import render

from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import send_mail
from datetime import datetime
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст
from .models import Appointment


class AppointmentView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'appointment/make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        # получаем наш html
        html_content = render_to_string(
            'appointment/appointment_created.html',
            {
                'appointment': appointment,
            }
        )

        msg = EmailMultiAlternatives(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            body=appointment.message,  # это то же, что и message
            from_email='preobrazhensky.evgenii@yandex.ru',
            to=[request.user.email],
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html
        msg.send()  # отсылаем
        return redirect('/')  # 'make_appointment'
