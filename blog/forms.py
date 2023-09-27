from django import forms
from .models import Post, Category, Profile, Comment

#choices = [('coding','coding'),('sports','sports'),('entertainment','entertainment')]
choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body', 'snippet', 'header_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'enter title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control','placeholder':'enter title_tag'}),
            'author': forms.TextInput(attrs={'class': 'form-control','placeholder':'enter title_tag', 'value':'', 'id':'elder', 'type':'hidden'}),
           # 'author': forms.Select(attrs={'class': 'form-control','placeholder':'enter author'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control','placeholder':'enter author'}),
            'body': forms.Textarea(attrs={'class': 'form-control','placeholder':'enter post'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control','placeholder':'enter post'}),


        }


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            #'profile_pic': forms.Select(attrs={'class': 'form-control', 'placeholder': 'enter title_tag'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            # 'author': forms.Select(attrs={'class': 'form-control','placeholder':'enter author'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter title'}),

        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),



        }