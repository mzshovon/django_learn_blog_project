from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import BlogPost, User
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
    paginate_by = 3
    ordering = ['-created_at']

class UserPostListView(ListView):
    model = BlogPost
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3
    ordering = ['-created_at']
    def get_queryset(self):
        user = get_object_or_404(User, username= self.kwargs.get('username'))
        return BlogPost.objects.filter(author= user).order_by('-created_at')
    

class PostDetailView(DetailView):
    model = BlogPost

class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title','content','post_image','tags']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ['title','content','post_image','tags']
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

def post_track_list(request):
    return render(request, 'blog/blogpost_track_post.html')