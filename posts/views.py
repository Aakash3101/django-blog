from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    if request.method == 'POST':
        print("POST")
        title = request.POST['title']
        body = request.POST['body']
        date = request.POST['date']
        Post.objects.create(title=title, body=body, created_at=date)
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post': post})


def create_post(request):
    return render(request, 'create_post.html')