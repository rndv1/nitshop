from django.shortcuts import render
from .models import Article

def blog(request):
    blog = Article.objects.order_by('-date')
    return render(request, 'nit/blog.html', {'blog':blog})
