from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from blog.models import Post
from .models import Comment, Reply
from .forms import CommentForm, ReplyForm
 
# Create your views here.

@login_required
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    
    if request.method == "POST":
      form = CommentForm(request.POST)
      if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.created_by = request.user
        comment.save()
        
        return redirect("commenting:detail", pk=post.id)
      
    else:
      form = CommentForm()
          
    return render(request, "commenting/detail.html", {
      "post": post,
      "comments": comments,
      "form": form
    })


@login_required    
def reply(request, comment_id):
  comment = get_object_or_404(Comment, pk=comment_id)
  replys = Reply.objects.filter(reply_to=comment)
  
  if request.method == "POST":
    form = ReplyForm(request.POST)
    
    if form.is_valid():
      comment_reply = form.save(commit=False)
      comment_reply.reply_to = comment
      comment_reply.created_by = request.user
      comment_reply.save()
      
      redirect("commenting:detail",pk=comment.post.id)
  
  else:
    form = ReplyForm()
    
  return render(request, "commenting/reply.html", {
    "comment": comment,
    "replys": replys,
    "form": form
  })
    