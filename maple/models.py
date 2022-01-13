from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Character(TimeStampedModel):
    RATE = (
        ("1", "1점"),
        ("1.5", "1.5점"),
        ("2", "2점"),
        ("2.5", "2.5점"),
        ("3", "3점"),
        ("3.5", "3.5점"),
        ("4", "4점"),
        ("4.5", "4.5점"),
        ("5", "5점"),
    )
    job = models.CharField(max_length=50,
                           db_index=True,
                           validators=[
                               MinLengthValidator(2),
                               RegexValidator(r"[ㄱ-힣]", message="한글을 입력해주세요.")
                           ],
                           verbose_name="직업"
                           )
    description = models.TextField(verbose_name="설명")
    photo = models.ImageField(blank=True, verbose_name="사진/일러")
    invincibility = models.BooleanField(default=True, verbose_name="무적기 보유 여부")
    bind = models.BooleanField(default=False, verbose_name="바인드 보유 여부")
    rush = models.BooleanField(default=False, verbose_name="돌진기 보유 여부")
    teleport = models.BooleanField(default=False, verbose_name="텔레포트 보유 여부")
    hunt_rating = models.CharField(max_length=1, choices=RATE, verbose_name="사냥 능력")
    raid_rating = models.CharField(max_length=1, choices=RATE, verbose_name="보스 성능")
