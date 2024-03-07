from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from blog.models import Blogpost


class BlogpostCreateView(CreateView):
    model = Blogpost
    fields = ('title', 'content', 'created_at', 'view_count')
    success_url = reverse_lazy('blog:blog_list')


class BlogpostListView(ListView):
    model = Blogpost
