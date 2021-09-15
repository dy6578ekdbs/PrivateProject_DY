from django.db.models.fields import BLANK_CHOICE_DASH
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, HashTag, Youtube
from django.utils import timezone
from .forms import BlogForm, CommentForm, YoutubeForm
# Create your views here.

def home(request):
    blog = Blog.objects
    return render(request, 'home.html', {'blogs':blog})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    blog_hashtag = blog_detail.hashtag.all()
    return render(request, 'detail.html', {'blog':blog_detail, 'hashtags':blog_hashtag})

def new(request):
    form = BlogForm()                           
    return render(request, 'new.html', {'form':form})

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid(): #폼 유효성 검사
        new_blog = form.save(commit=False) #임시저장을 위함
        new_blog.pub_date = timezone.now()
        new_blog.author = request.user
        new_blog.save()
        hashtags = request.POST['hashtags']
        hashtag = hashtags.split(",")
        for tag in hashtag:
            ht = HashTag.objects.get_or_create(hashtag_name=tag)
            new_blog.hashtag.add(ht[0])
        return redirect('detail', new_blog.id) 
    return redirect('home')
   

def edit(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'blog' : blog_detail})

def update(request, blog_id):
    blog_update = get_object_or_404(Blog, pk=blog_id)
    blog_update.title = request.POST['title']
    blog_update.body = request.POST['body']
    blog_update.save()
    return redirect('home')

def delete(request, blog_id):
    blog_delete = get_object_or_404(Blog, pk=blog_id)
    blog_delete.delete()
    return redirect('home')


def add_comment_to_post(request, blog_id): #댓글
    blog = get_object_or_404(Blog, pk = blog_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            return redirect('detail', blog_id)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html',{'form':form})


def create_youtube(request, blog_id): #유튜브 게시글 추가
    blog = get_object_or_404(Blog, pk = blog_id)
    if request.method == "POST":
        form = YoutubeForm(request.POST)
        if form.is_valid():
            youtube = form.save(commit=False)
            youtube.post = blog
            youtube.save()
            return redirect('detail', blog_id)
    else:
        form = YoutubeForm()
    return render(request, 'create_youtube.html',{'form':form})


def delete_youtube(request, blog_id, youtube_id): #삭제하기
    youtube_delete = Youtube.objects.get(id = youtube_id)
    youtube_delete.delete()
    return redirect('detail', blog_id)

def edit_youtube(request, youtube_id, blog_id):  #영상 수정 페이지로 이동
    youtube_detail = Youtube.objects.get(id = youtube_id)
    return render(request, 'edit_youtube.html', {'youtube' : youtube_detail})

def update_youtube(request,youtube_id): #수정하기
    youtube_update = Youtube.objects.get(id = youtube_id)
    youtube_update.subtitle = request.POST['subtitle']
    youtube_update.body = request.POST['body']
    youtube_update.url = request.POST['url']
    youtube_update.save()
    return redirect('home')
