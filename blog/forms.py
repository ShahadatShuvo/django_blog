from django import forms
from blog.models.post import Comment, Post
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = [
            'title',
            'overview',
            'thumbnail',
            'categories',
            'content',
            'featured',
            'previous_post',
            'next_post'
        ]


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': "Type your comment",
        'id': 'usercomment',
        'rows': '4'
    }))

    class Meta:
        model = Comment
        fields = ('content',)

