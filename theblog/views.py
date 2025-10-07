import random
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date']

    def get_queryset(self):
        qs = list(Post.objects.all())
        random.shuffle(qs)
        return qs

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields=['title','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url= reverse_lazy('home')
    

#from django.shortcuts import render, get_object_or_404
#from django.views.generic import ListView, DetailView, CreateView
#from .models import Post
from .forms import PostForm
#def home(request):
    #return render(request, 'home.html')

#class HomeView(ListView):
    #model=Post
    #template_name= 'home.html'
    #context_object_name='posts'
    #ordering= ['-date']
#class ArticleDetailView (DetailView):
    #model=Post
    #template_name='article_detail.html'
#class AddPostView(CreateView):
    #model=Post
    #form_class=PostForm
    #template_name='add_post.html'
    # fields= '__all__'
    # fields= ('title', 'body')