from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import ListView , DetailView, CreateView, UpdateView, DeleteView, DetailView
from .models import Post, signup, Category, Profile, Comment
from .forms import PostForm, ProfilePageForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponseRedirect

# Create your views here.
#def home(request):
    #return render(request,'home.html',{})


def postComment(request):
    if request.method == "POST":
        coment = request.POST['coment']
        user = auth.authenticate(coment=coment)
    else:
        return render(request, "article_details.html", {})






def search(reequest):
    if reequest.method == "POST":
        searched = reequest.POST['searched']
        bar = Post.objects.filter(body__contains=searched)
        barr = Post.objects.filter(title__contains=searched)
        return render(reequest,'search.html',{'searched':searched,'bar':bar,'barr':barr})
    else:
        return render(reequest, 'search.html', {})

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    #fields = ('title','body')
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')


class EditProfilePageView(generic.UpdateView):
    model = Profile

    template_name = 'edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url']
    success_url = reverse_lazy('home')

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'create_user_profile_page.html'
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'user_profile.html'

    def get_context_data(self, *args, **kwargs):

        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context



def edit_profile(request,id):
    edt = User.objects.get(pk=id)
    if request.method == "POST":
        #if len(request.FILES) !=0:
            edt.first_name = request.POST.get('first_name')
            edt.last_name = request.POST.get('last_name')
            edt.username = request.POST.get('username')
            edt.email = request.POST.get('email')


            edt.save();
            print('updated')
            return redirect('/')

    #context = {'edt':edt}
    return render(request,'edit_profile.html', {'edt':edt})






def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))



class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):

        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleView(DetailView):
    model = Post

    template_name = 'article_details.html'



    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context






class AddView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title','body')

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    # fields = ('title','body')

def CategoryView(request,cats):
    category_post = Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'category.html',{'cats':cats.title().replace('-',' '), 'category_post':category_post})

class UpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    #fields = ['title','title_tag','body']







class DeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['passwor']
        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username, email=email, password=password1)
        user.save();
        print("data printed")
        return redirect('login')
    else:
        return render(request,'register.html',{})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print('invalid credentials')
            return redirect('login')
    else:
        return render(request,"login.html",{})

def logout(request):
    auth.logout(request)
    return redirect('/')




