from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

def home(request):
    return render(request, 'blog/home.html')

def blog(request):
    posts = Post.objects.all().order_by('-date_posted')
    comments = []
    for post in posts:
        post.p_comments = []
        post_comments = Comment.objects.filter(post=post).order_by('-date_posted')[:3]
        for comment in post_comments:
            post.p_comments.append(comment)

    context = {
        'posts': posts,
        'title': 'Blog',
        'comments': comments
    }

    return render(request, 'blog/blog.html', context)

class PostDetailView(DetailView):
    model = Post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
    
    def handle_no_permission(self):
        messages.warning(self.request, f"User does not have blog admin access.")
        return redirect(reverse_lazy('blog-blog'))
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        # Get the post object using the pk from the URL
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)

        # Assign the author and post to the comment instance
        form.instance.author = self.request.user
        form.instance.post = post

        return super().form_valid(form)

def portfolio(request):
    return render(request, 'blog/portfolio.html', {'title': 'Portfolio'})

def all_comments(request, post_id):
    #We iterate over the posts till we get the post with its ID from the database of post
    #This will change when we have an actual database and can index each post
    
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post).order_by('date_posted')
    
    context = {
        'post': post,
        'title': 'Comments',
        'comments': comments
    }

    return render(request, 'blog/comments.html', context)


def pdf_view(request):
    try:
        return FileResponse(open('media/Reuven Israeli CV.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()