from django import forms
from .models import Post, Tag

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'article', 'name', 'image']
        
    title = forms.TextInput()
    description = forms.TextInput()
    article = forms.Textarea()
    name = forms.Select()
    image = forms.FileInput()
    
    
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'article', 'image']
        
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "description": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "article": forms.Textarea(attrs={
                "class": "form-control"
            }),
            "image": forms.FileInput(attrs={
                "class": "form-control"
            })
        }
        
