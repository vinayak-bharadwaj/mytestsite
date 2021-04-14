from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import post

#home function if to mange the trafic users see this when sent to the route.
#to pass html using templates we create a template directory.
#the syntax of render is(request, subdir_oftemplates_name/html_file)

posts=[
    {
        'author':'Itachi1123',
        'title':'Blog post1 ',
        'content':'First post content...',
        'date_posted':'Dec 12 2020'
    },
    {
        'author':'sudo_name',
        'title':'blog post 2',
        'content':'Second post content',
        'date_posted':'13 Dec 2020'
    }
]
#here we assume that we made a request an got back the following list of Dic from the Data base
def home(request):
    context={
    #    'posts': posts
         'posts' :post.objects.all()
    }
    return render(request ,'blog/home.html',context)#third arg makes the key name acceseble in the template

def about(request):
    return render(request ,'blog/about.html',{'title': 'About'})

class PostListView(ListView):
    model = post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
