from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse  # импортируем респонс для проверки текста


from django.utils.translation import activate, get_supported_language_variant


import pytz
from news.models import Post


from django.utils import timezone
from django.shortcuts import redirect

# def index(request):
#     return render(request, 'news/index.html')


class Index(View):

    def get(self, request):
        current_time = timezone.now()
        models = Post.objects.all()
        context = {
            'models': models,
            'current_time': timezone.now(),
            'timezones': pytz.common_timezones  # добавляем в контекст все доступные часовые пояса
        }
        return HttpResponse(render(request, 'news/index.html', context))

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
