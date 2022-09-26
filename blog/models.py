from django.db import models
from django.utils.text import slugify
from account.models import User
class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'نام مدرس' )
    image = models.ImageField(upload_to='Author_image', verbose_name = 'تصویر' )
    discripsion = models.TextField(null=True, blank=True, verbose_name = 'درباره ی مدرس' )
    instagram = models.TextField(null=True, blank=True, verbose_name = 'ادرس اینستاگرام' )
    github = models.TextField(null=True, blank=True, verbose_name = 'ادرس گیت هاب' )
    linkdin = models.TextField(null=True, blank=True, verbose_name = 'ادرس لینکدین' )
    twwiter = models.TextField(null=True, blank=True, verbose_name = 'ادرس توییتر' )
    created = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering =('-created',)
        verbose_name_plural = 'مدرسان'

class Categories(models.Model):
    title = models.CharField(max_length=50,null=True, blank=True, verbose_name = 'اسم دسته بندی' )
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering =('-created',)
        verbose_name_plural = 'دسته بندی ها'
class Tags(models.Model):
    title = models.CharField(max_length=50 , null=True, blank=True , verbose_name = 'اسم تگ' )
    created = models.DateTimeField(auto_now_add=True , verbose_name = 'زمان تولید' )
    def __str__(self):
        return self.title
    class Meta:
        ordering =('-created',)
        verbose_name_plural = 'تگ ها'

class Post(models.Model):
    author = models.ForeignKey(Author , on_delete=models.CASCADE , verbose_name = 'نام مدرس' )
    categories = models.ManyToManyField(Categories , help_text="دسته بندی" , related_name="posts", verbose_name = 'دسته بندی ها' )
    tag = models.ManyToManyField(Tags , help_text="دسته بندی", verbose_name = 'تگ ها' )
    title = models.CharField(max_length=50, verbose_name = 'اسم پست به اینگلیسی و اصلی' )
    title2 = models.CharField(max_length=50, verbose_name = 'اسم پست نمایشی به فارسی' )
    discripsion = models.TextField(verbose_name = 'توضیحات' )
    video = models.FileField(null=True, blank=True , upload_to='Post_video', verbose_name = 'ویدیو' )
    image = models.ImageField(null=True, blank=True , upload_to='Post_image', verbose_name = 'عکس پست' )
    time = models.IntegerField(null=True, blank=True, verbose_name = 'مدت زمان پست' )
    views = models.IntegerField(default=0, verbose_name = 'دیده شده ها' )
    created = models.DateField(null=True, blank=True , auto_now_add=True)
    updated = models.DateField(null=True, blank=True , auto_now=True)
    slug = models.SlugField(null=True, blank=True , unique=True , allow_unicode=True, verbose_name = 'اسلاگ' )


    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'پست ها'

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
    user = models.ForeignKey(User , related_name='notifications' , on_delete=models.CASCADE , verbose_name = 'کاربر ها' )
    body = models.TextField(null=True, blank=True, verbose_name = 'توضیحات' )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body
    
    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'اعلان ها'

