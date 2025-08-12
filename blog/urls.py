from django.urls import path
from .views import PostDetailView, PostCreateView, CommentCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('pdfview/', views.pdf_view, name='pdf-view'),
    path('blog/', views.blog, name='blog-blog'),
    path('portfolio/', views.portfolio, name='blog-portfolio'),
    path('all_comments/<int:post_id>/', views.all_comments, name='all_comments'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]