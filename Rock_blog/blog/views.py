from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm, EditPostForm
from .models import Post

# Create your views here.

@login_required
def create(request):
    if request.method=="POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            
            return redirect("base:index")
    else:
        form = BlogPostForm()
        
    return render(request, 'blog/create.html', {'form': form})

@login_required
def update(request,pk):
    post = get_object_or_404(Post, pk=pk, created_by=request.user)
    
    if request.method=="POST":
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.save()
            
            redirect("base:index")
    else:
        form = EditPostForm(instance=post)
        
    return render(request, 'blog/update.html',{'form': form})

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk, created_by=request.user)
    post.delete()
    
    return redirect("base:index")
