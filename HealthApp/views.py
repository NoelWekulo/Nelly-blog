from django.shortcuts import render, redirect
from HealthApp.models import BlogCategory, Blog, Comment
from HealthApp.forms import CommentForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')

def blog(request):
    blogs = Blog.objects.all().order_by('-date_posted')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog.html', context)

def cart(request):
    return render(request, 'cart.html')

def category(request):
    return render(request, 'category.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def search_result(request):
    return render(request, 'search_result.html')

def shop(request):
    return render(request, 'shop.html')

def single(request, slug):
    blog = Blog.objects.get(slug=slug)
    # Handle comment submission
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('blog_detail', slug=slug)
    
    comments = Comment.objects.filter(blog=blog).order_by('-added_at')
    context = {
        'blog': blog,
        'comments': comments,
        'form': CommentForm()
    }
    return render(request, 'single.html', context)

def thankyou(request):
    return render(request, 'thankyou.html')

