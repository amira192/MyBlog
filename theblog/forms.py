from django import forms
from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=('title','author', 'body','image') 

        widgets= {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title placeholder stuff'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your comment here...',
            }),
        }
        labels = {
            'body': '', 
        }