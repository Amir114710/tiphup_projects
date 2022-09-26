# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from .models import Post

# @receiver(pre_save , sender=Post)
# def create_post(sender , instance , *args, **kwargs):
#     if not instance.slug:
#         instance.slug = ""

# def create_uniqe_slug(instance , newslug=None):
