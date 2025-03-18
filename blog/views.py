from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "list.html"
    context_object_name = "posts"
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        context["paginator"] = paginator

        page = self.request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
            
        context["posts"] = posts
        
        return context

    
class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "detail.html"
    context_object_name = "post"

    def get_object(self):
        return get_object_or_404(Post, title=self.kwargs['title'])











# from django.shortcuts import render, get_object_or_404
# from .models import Post
# # Create your views here.
# def index(request):
#     return render(request, 'index.html')

# def blog_list(request):
#     posts = Post.objects.all()

#     return render(request, "list.html", {"posts": posts})


# def blog_detail(request, title):
    
#     post = get_object_or_404(Post, title=title)
    
#     return render(request, "detail.html", {"post": post})