from django.shortcuts import render
from django.views.generic.base import TemplateView 
from blog.models import Post , Categories , Like
# from django.http.response import JsonResponse, HttpResponse
# from django.views.decorators.http import require_GET, require_POST
# from django.shortcuts import get_object_or_404
# from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
# from webpush import send_user_notification
# import json
class HomeView(TemplateView):
    template_name = 'home_app/index.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = Post.objects.all()[:6]
        context['post_likes'] = Like.objects.all()[:6]
        context['Categories'] = Categories.objects.all()
        return context

# @require_POST
# @csrf_exempt
# def send_push(request):
#     try:
#         body = request.body
#         data = json.loads(body)

#         if 'head' not in data or 'body' not in data or 'id' not in data:
#             return JsonResponse(status=400, data={"message": "Invalid data format"})

#         user_id = data['id']
#         user = get_object_or_404(User, pk=user_id)
#         payload = {'head': data['head'], 'body': data['body']}
#         send_user_notification(user=user, payload=payload, ttl=1000)

#         return JsonResponse(status=200, data={"message": "Web push successful"})
#     except TypeError:
#         return JsonResponse(status=500, data={"message": "An error occurred"})