from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorators import Article_ownership_required
from articleapp.form import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm


@method_decorator(login_required, 'get')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        article_profile = form.save(commit=False)
        article_profile.writer = self.request.user
        article_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})



class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    template_name = 'articleapp/detail.html'
    context_object_name = 'target_article'


@method_decorator(Article_ownership_required, 'get')
@method_decorator(Article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(Article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articleapp/delete.html'
    success_url = reverse_lazy('articleapp:list')
    context_object_name = 'target_article'

class ArticleListView(ListView):
    model = Article
    template_name = 'articleapp/list.html'
    context_object_name = 'article_list'
    paginate_by = 1


