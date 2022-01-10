from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"  # 실서비스에서는 비추

