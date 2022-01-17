from django import forms

from news.models import Article


# 장고 딴에서 웹 구현시 폼 에서 유효성 검사
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title:
            if len(title) < 3:
                raise forms.ValidationError("3글자 이상!!")
            return title
