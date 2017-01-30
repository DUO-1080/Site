from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields = ['user_name','body']
        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'nickname form-control',
                'placeholder':'nickname',

            }),
            'body':forms.Textarea(attrs={
                'class':'from-control size-control',
                'placeholder':'评论内容',
                'rows':4
            }),
        }