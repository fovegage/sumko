# Generated by Django 2.1 on 2019-07-21 13:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_auto_20190721_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='goods.GoodCategory', verbose_name='商品分类'),
            preserve_default=False,
        ),
    ]