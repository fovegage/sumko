# Generated by Django 2.1 on 2019-07-23 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_auto_20190722_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodcarouselimage',
            name='good',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='goods.Good', verbose_name='所属商品'),
        ),
    ]
