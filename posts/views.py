from django.shortcuts import render,redirect
from .models import Post
from .forms import RandomPostGeneratorForm
from .tasks import create_random_posts
from django.contrib import messages

def posts_view(request):
    posts = Post.objects.all()
    return render(request,'posts.html',{'posts':posts})


def generate_view(request):
    form = RandomPostGeneratorForm(request.POST)
    if form.is_valid():
        number_of_posts = form.cleaned_data.get('number_of_posts')
        create_random_posts.delay(number_of_posts)
        messages.success(request,'random posts generated refresh the page')
        return redirect('posts')
    return render(request,'generate.html',{'form':form})    