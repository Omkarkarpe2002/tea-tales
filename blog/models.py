from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.html import linebreaks

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    typeofbook=models.CharField(max_length=50, default="")
    author=models.CharField(max_length=14)
    bookauthor=models.CharField(max_length=100, default="")
    bookrating=models.CharField(max_length=50, default="")
    booktagline=models.CharField(max_length=1000, default="")
    content=models.TextField()
    image = models.ImageField(upload_to='post', null=True, blank=True)
    slug=models.CharField(max_length=130)
    views= models.IntegerField(default=0)
    timeStamp=models.DateTimeField(blank=True)

    def formatted_content(self):
        return linebreaks(self.content)

    def __str__(self):
        return self.title + " by " + self.author

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username

# class Addblog(models.Model):
#     sno= models.AutoField(primary_key=True)
#     title=models.CharField(max_length=255)
#     author=models.CharField(max_length=14)
#     slug=models.CharField(max_length=130)
#     content=models.TextField()


    
