from django.contrib.auth.models import User
from django.db import models
from blog.models import Post

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comment_post", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name="comment_user", on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f"Comment by {self.created_by.username} to {self.post.title}"
        
        
class Reply(models.Model):
    reply_to = models.ForeignKey(Comment, related_name="reply_to", on_delete=models.CASCADE)
    body = models.TextField()
    created_by = models.ForeignKey(User, related_name="replyer", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_by',)
        
    def __str__(self):
        return f"Reply to {self.reply_to.created_by} by {self.created_by.username} on post {self.reply_to.post}"
        
    
