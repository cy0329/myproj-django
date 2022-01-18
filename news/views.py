import json

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet  # <-- 아랫줄 하나하나가 다 포함되있는 부모
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveAPIView,
)
from news.models import Article
from news.serializers import (
    ArticleSerializer,
)  # ArticleAnonymousSerializer, ArticleGoldMembershipSerializer,


# list, detail, create, update, delete 를 1개 ViewSet에서 지원
# 나눠서 리스트, 디테일은 아무때나 조회 가능, 나머지는 인증 됐을 때만
# request type에 따라
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [AllowAny]  # DRF 디폴트 설정
    # permission_classes = [IsAuthenticated]
    # 위 주석 한줄과 아래는 같은 결과

    def get_permissions(self):
        # if self.request.method in ("POST", "PUT", "PATCH", "DELETE"):
        if self.request.method == "GET":
            # 각각을 언제 쓰느냐를 잘 봐
            return [AllowAny()]
        return [IsAuthenticated()]




    # def get_serializer_class(self):
    #     # return ArticleSerializer
    #     # return ArticleAnonymousSerializer
    #     # return ArticleGoldMembershipSerializer
    #     return ArticleAdminSerializer

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #
    #     query = self.request.query_params.get("query", "")
    #     if query:
    #         qs = qs.filter(title__icontains=query)
    #
    #     year = self.request.query_params.get("year", "")
    #     if year:
    #         qs = qs.filter(created_at__year=year)
    #     return qs


# article_list = ListAPIView.as_view(
#     queryset=Article.objects.all(),
#     serializer_class=ArticleSerializer,
# )

# step 1
# def article_list(request):
#     qs = Article.objects.all()
#
#     # 2
#     serializer = ArticleSerializer(qs, many=True)
#     data = serializer.data
#
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
