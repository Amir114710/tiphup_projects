from django.contrib import admin
from .models import Author , Categories , Tags , Post , Like , Comments , Notification

admin.site.register(Author)
admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comments)
admin.site.register(Notification)
