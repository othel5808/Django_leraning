from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from articleapp.models import Article
from profileapp.models import Profile


def Article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        # temp_Profile =
        return func(request, *args, **kwargs)
    return decorated
