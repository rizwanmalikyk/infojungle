from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Post, Comment


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget(

         )  
     )
    class Meta:
        model = Post
        fields = ('title', 'overview', 'content', 'thumbnail',
                    'categories', 'featured', 'previous_post', 'next_post')


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    
    class Meta:
        model = Comment
        fields = ('content', )
