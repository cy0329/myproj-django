# Generated by Django 3.2.11 on 2022-01-16 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maple', '0002_auto_20220116_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('전사', '전사'), ('마법사', '마법사'), ('궁수', '궁수'), ('도적', '도적'), ('해적', '해적')], db_index=True, max_length=10, unique=True, verbose_name='직업군'),
        ),
        migrations.AlterField(
            model_name='character',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='maple.category', verbose_name='직업군'),
        ),
    ]
