from django.urls import path

from blog.views import BlogpostCreateView, BlogpostListView

app_name = 'blog'


urlpatterns = [
     path('create/', BlogpostCreateView.as_view(), name='create'),
     path('blog_list/', BlogpostListView.as_view(), name='blog_list'),
    # path('view/<int:pk>/', MaterialDetailView.as_view(), name='view'),
    # path('edit/<int:pk>/', MaterialUpdateView.as_view(), name='edit'),
    # path('delete/<int:pk>/', MaterialDeleteView.as_view(), name='delete'),
]