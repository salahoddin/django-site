from cProfile import label
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = [__all__]
        exclude = ['post']
        labels = {
            'user_name': 'Your name',
            'user_email': 'Your email',
            'comment_text': 'Your comment'
        }
