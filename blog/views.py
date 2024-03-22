from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from home.models import Addblog
from django.contrib import messages
from django.contrib.auth.models import User
from blog.templatetags import extras
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def blogHome(request): 
    allPosts= Post.objects.all().order_by('-timeStamp')
    alld=Addblog.objects.all()

    paginator = Paginator(allPosts, 6)
    page_number = request.GET.get('page')
    try:
        allPosts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        allPosts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        allPosts = paginator.page(paginator.num_pages)


    context={'allPosts': allPosts,'postn':alld}
    return render(request, "blog/blogHome.html", context)



def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    post.views= post.views +1
    post.save()    
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")

