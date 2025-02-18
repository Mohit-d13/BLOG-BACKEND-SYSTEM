from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm
from blog.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'base/index.html', {
        'posts': posts,
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect('/')
            
    else:
        form = SignupForm()
            
    return render(request, 'base/signup.html', {
        'form': form,
    })
    