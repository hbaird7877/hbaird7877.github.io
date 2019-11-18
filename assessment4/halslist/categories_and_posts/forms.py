from django import forms
from .models import Category, Post

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'creation_date')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'post_title', 'poster_name', 'creation_date', 'post_text', 'telephone', 'email', 'price')

