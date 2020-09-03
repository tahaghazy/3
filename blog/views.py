from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.db.models import F
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *




def home(request):
    categories = Category.objects.all()

    context = {
        'categories': categories

    }

    return render(request, 'home.html', context)

def category(request,slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category,slug=slug)
    post = category.posts.filter(active=True)
    paginator = Paginator(post, 6)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_page)

    context = {
        'categories': categories,
        'post':post

    }

    return render(request, 'category.html', context)


def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    context = {
        'title': post.title,
        'post': post,
    }

    return render(request, 'detail.html', context)

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'new_post.html'
    form_class = PostCreateForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostCreateForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        success_url = '/profile/'

        if self.request.user == post.author:
            return True

        return False

def rfha(request):
    post = PostS.objects.filter(active=True)
    context = {
        'post':post
    }
    return render(request, 'rfha.html', context)





def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(content__icontains=query)

            results= Post.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')