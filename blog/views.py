from django.shortcuts import render,get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)  
    return render(request, 'blog/post_detail.html', {'post':post})

@login_required
def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.author:
        return redirect('post_list')
    else:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)

        else:
            form = PostForm(instance=post) 
    return render(request, 'blog/post_edit.html', {'form':form})    

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def signup(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')

    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form':form})    


from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
  
# Create your views here. 
def hotel_image_view(request): 
  
    if request.method == 'POST': 
        form = HotelForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('image_list') 
    else: 
        form = HotelForm() 
    return render(request, 'blog/hotel_image_form.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 

# Python program to view  
# for displaying images 
  
def display_hotel_images(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        Gallerys = Gallery.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        Hotels = Gallery.objects.all()  
        return render(request, 'blog/image_list.html', {'hotel_images' : Hotels})

