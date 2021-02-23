from django.shortcuts import render
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
   