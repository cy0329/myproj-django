import json

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet  # <-- 아랫줄 하나하나가 다 포함되있는 부모
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from news.models import Article
from news.serializers import ArticleSerializer # ArticleAnonymousSerializer, ArticleGoldMembershipSerializer, ArticleAdminSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # def get_serializer_class(self):
    #     return ArticleSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query)

        year = self.request.query_params.get("year", "")
        if year:
            qs = qs.filter(created_at__year=year)
        return qs

# article_list = ListAPIView.as_view(
#     queryset=Article.objects.all(),
#     serializer_class=ArticleSerializer,
# )

# def article_list(request):
#     qs = Article.objects.all()
#     serializer = ArticleSerializer(qs, many=True)
#     data = serializer.data
#     # data = [
#     #     {
#     #         "id": article.id,
#     #         "title": article.title,
#     #         "content": article.content,
#     #         "photo": request.build_absolute_uri(article.photo.url) if article.photo else None,
#     #     }
#     #     for article in qs
#     # ]
#     json_string = json.dumps(data)
#     return HttpResponse(json_string)
