from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from news.models import Comment

APP = 'news/'


class CommentList(ListView):
    model = Comment
    ordering = 'comment_time_in'
    template_name = APP + 'comments.html'
    context_object_name = 'comments'
