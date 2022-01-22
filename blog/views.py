import json

from django.http import HttpResponse
from rest_framework import viewsets
from blog.models import Post
from blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query)
        return qs


# def post_list(request):
#     qs = Post.objects.all()
#     data = [
#         {
#             "id": post.id,
#             "title": post.title,
#             "content": post.content,
#             "photo": request.build_absolute_uri(post.photo.url) if post.photo else None,
#         }
#         for post in qs
#     ]
#     json_string = json.dumps(data)
#     return HttpResponse(json_string)
