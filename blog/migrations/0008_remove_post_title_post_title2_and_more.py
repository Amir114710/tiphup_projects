# Generated by Django 4.0.3 on 2022-09-26 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_alter_author_options_alter_categories_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='title2',
            field=models.CharField(default=1, max_length=50, verbose_name='اسم پست نمایشی به فارسی'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='discripsion',
            field=models.TextField(blank=True, null=True, verbose_name='درباره ی مدرس'),
        ),
        migrations.AlterField(
            model_name='author',
            name='github',
            field=models.TextField(blank=True, null=True, verbose_name='ادرس گیت هاب'),
        ),
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(upload_to='Author_image', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='author',
            name='instagram',
            field=models.TextField(blank=True, null=True, verbose_name='ادرس اینستاگرام'),
        ),
        migrations.AlterField(
            model_name='author',
            name='linkdin',
            field=models.TextField(blank=True, null=True, verbose_name='ادرس لینکدین'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, verbose_name='نام مدرس'),
        ),
        migrations.AlterField(
            model_name='author',
            name='twwiter',
            field=models.TextField(blank=True, null=True, verbose_name='ادرس توییتر'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='اسم دسته بندی'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='body',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL, verbose_name='کاربر ها'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author', verbose_name='نام مدرس'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(help_text='دسته بندی', related_name='posts', to='blog.categories', verbose_name='دسته بندی ها'),
        ),
        migrations.AlterField(
            model_name='post',
            name='discripsion',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Post_image', verbose_name='عکس پست'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(help_text='دسته بندی', to='blog.tags', verbose_name='تگ ها'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.IntegerField(blank=True, null=True, verbose_name='مدت زمان پست'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='Post_video', verbose_name='ویدیو'),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0, verbose_name='دیده شده ها'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان تولید'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='اسم تگ'),
        ),
    ]
