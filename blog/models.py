from django.db import models
from django.utils.text import slugify
from account.models import User
class Author(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Author_image')
    discripsion = models.TextField(null=True, blank=True)
    instagram = models.TextField(null=True, blank=True)
    github = models.TextField(null=True, blank=True)
    linkdin = models.TextField(null=True, blank=True)
    twwiter = models.TextField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering =('-created',)
class Categories(models.Model):
    title = models.CharField(max_length=50,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering =('-created',)
class Tags(models.Model):
    title = models.CharField(max_length=50 , null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering =('-created',)
class objects_manager(models.Manager):
    def like_click(self):
        return self.filter(like_click=True)
class Post(models.Model):
    author = models.ForeignKey(Author , on_delete=models.CASCADE )
    categories = models.ManyToManyField(Categories , help_text="دسته بندی" , related_name="posts")
    tag = models.ManyToManyField(Tags , help_text="دسته بندی")
    title = models.CharField(max_length=50)
    discripsion = models.TextField()
    video = models.FileField(null=True, blank=True , upload_to='Post_video')
    image = models.ImageField(null=True, blank=True , upload_to='Post_image')
    time = models.IntegerField(null=True, blank=True)
    views = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    like_click = models.BooleanField(default=False)
    objects = objects_manager()
    created = models.DateField(null=True, blank=True , auto_now_add=True)
    updated = models.DateField(null=True, blank=True , auto_now=True)
    slug = models.SlugField(null=True, blank=True , unique=True , allow_unicode=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post , self).save(*args, **kwargs)

class Like(models.Model):
    users = models.ForeignKey(User, related_name='likes2' , on_delete=models.CASCADE , verbose_name = 'کاربر')
    posts = models.ForeignKey(Post, related_name='likes2' , on_delete=models.CASCADE , verbose_name = 'مقاله')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.users.email} - {self.posts.title}"

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها"
        ordering = ("-created",)


class Comments(models.Model):
    user = models.ForeignKey(User , related_name="comment" , on_delete=models.CASCADE)
    posts = models.ForeignKey(Post, related_name="comment" , on_delete=models.CASCADE)

    parent = models.ForeignKey('self' , on_delete=models.CASCADE , related_name = 'replies' , null=True , blank=True)

    message = models.CharField(max_length=50 , null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email}-{self.posts.title}'

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
        ordering = ('-created',)
    

class Notification(models.Model):
    user = models.ForeignKey(User , related_name='notifications' , on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body
    
    class Meta:
        ordering = ('-created_at',)

