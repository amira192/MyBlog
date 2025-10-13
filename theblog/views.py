import random
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.db.models import Q

class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
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
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all().order_by('-date')
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not request.user.is_authenticated:
          return redirect('login') 
    
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect('article_detail', pk=self.object.pk)
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

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.user in post.likes.all():
        post.likes.remove(request.user)  
    else:
        post.likes.add(request.user)     

    return redirect('article_detail', pk=pk)
    

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