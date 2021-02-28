from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import BlogPost
# Create your views here.
posts = [
            {
                'name':'intro',
                'id':hash('makeaquery')
            },
            {
                'name':'intro-1',
                'id':hash('makeaquerysss')
            }
        ]
def home(request):

    title = "Home"
    context = {
            'posts':BlogPost.objects.all(),
            'title':title
    }
    return render(request, 'blog/home.html',context)

class PostListView(ListView):
    model = BlogPost
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = BlogPost

class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ['title']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post  = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    success_url = '/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post  = self.get_object()
        if self.request.user == post.author:
            return True
        return False
