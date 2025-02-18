from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=150) 

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=500)
    article = models.TextField()
    name = models.ForeignKey(Tag, related_name='tag', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    created_by = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add='True')
    
    def __str__(self):
        return self.title
    
    
