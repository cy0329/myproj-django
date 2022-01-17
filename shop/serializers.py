# from django import forms
from rest_framework import serializers
from shop.models import Review

# 이건 장고만을 써서 구현하는 방법
# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
