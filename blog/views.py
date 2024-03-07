from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blogpost


class BlogpostCreateView(CreateView):
    model = Blogpost
    fields = ('title', 'content')
    success_url = reverse_lazy('blog:blog_list')


class BlogpostListView(ListView):
    model = Blogpost


class BlogpostDetailView(DetailView):
    model = Blogpost


class BlogpostUpdateView(UpdateView):
    model = Blogpost
    fields = ('title', 'content')
    success_url = reverse_lazy('blog:blog_list')


class BlogpostDeleteView(DeleteView):
    model = Blogpost
    success_url = reverse_lazy('blog:blog_list')
