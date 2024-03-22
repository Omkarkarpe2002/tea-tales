from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from home.models import Contact
from home.models import Addblog
from django.http import HttpResponseNotAllowed
from django.contrib import messages 
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User 
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth  import authenticate,  login, logout
from blog.models import Post


def home(request):
    latest_posts = Post.objects.order_by('-timeStamp')[0:3]
    return render(request, 'home/home.html', {'latest_posts': latest_posts})


def contact(request):
    name = ""
    email = ""
    phone = ""
    content = ""

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')

        # Check if any of the required fields are empty or None
        if not all([name, email, phone, content]):
            messages.error(request, "Please fill all the fields correctly")
        else:
            # Validate each field individually
            if len(name) < 2 :
                messages.error(request, "Name should be at least 2 characters long")
            else:
                try:
                    validate_email(email)
                except ValidationError:
                    messages.error(request, "Invalid email address")
            if len(phone) < 10 or len(phone) > 10:
                messages.error(request, "Phone number should be 10 characters long")
            if len(content) < 4:
                messages.error(request, "Content should be at least 4 characters long")

            # Process the form data if no errors
            if not messages.get_messages(request):
                # Additional validation if needed

                # Process the form data
                contact = Contact(name=name, email=email, phone=phone, content=content)
                contact.save()
                messages.success(request, "Your message has been successfully sent! Thankyou!")

    return render(request, "home/contact.html")

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        # allPostsTypeOfBook= Post.objects.filter(type__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)

def handleSignUp(request):
    
    def redirectWithError(redirect_url, error_message):
        if redirect_url:
            messages.error(request, error_message)
            messages.debug(request, f"Redirecting to: {redirect_url}")
            return redirect(redirect_url)
        else:
            messages.error(request, error_message)
            return redirect("home")

    if request.method == "POST":
        # Get the post parameters
        username = request.POST.get('username')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # Get the next URL if present
        next_url = request.POST.get('next') or request.GET.get('next')

        # Check for erroneous input
        if len(username) > 30:
            return redirectWithError(next_url, "Your username must be under 30 characters")

        if not username.isalnum():
            return redirectWithError(next_url, "Username should only contain letters and numbers")

        if pass1 != pass2:
            return redirectWithError(next_url, "Passwords do not match")

        if len(pass1) < 6:
            return redirectWithError(next_url, "Password should be at least 6 characters long")

        try:
            validate_email(email)
        except ValidationError:
            return redirectWithError(next_url, "Invalid email address")

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been successfully created!")
        if next_url:
            return HttpResponseRedirect(next_url)
        else:
            return redirect("home")

    else:
        return redirect('home')  # Redirect to home if not a POST request


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        next_url = request.POST.get('next') or request.GET.get('next')
        loginpassword=request.POST['loginpassword']


        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            if next_url:
                return redirect(next_url)
            else:
                return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            if next_url:
                return redirect(next_url)
            else:
                return redirect("home")

    return HttpResponse("404- Not found")

def handleLogout(request):
    if request.method == 'GET':
        next_url = request.GET.get('next')
        logout(request)
        messages.success(request, "Successfully logged out")
        if next_url:
            return redirect(next_url)
        else:
            return redirect("home")
    else:
        return HttpResponseNotAllowed(['GET'])



def about(request): 
    return render(request, "home/about.html")

def addblog(request):
    if request.method=="POST":
        # sno=request.POST['sno']
        title=request.POST['title']
        typeofbook=request.POST['type']
        author=request.POST['author']
        image = request.POST['image']
        booktagline=request.POST['booktagline']
        slug=request.POST['slug']
        content =request.POST['content']
        addblog=Addblog( title=title, typeofbook=typeofbook, author=author, slug=slug, content=content, image=image, booktagline=booktagline)
        addblog.save()
        messages.success(request, "Your message has been successfully sent")
    return render(request, "home/addblog.html")
