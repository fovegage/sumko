# Generated by Django 2.1 on 2019-07-24 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0003_auto_20190724_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payinfo',
            name='pay_sn',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='支付编号'),
        ),
    ]
