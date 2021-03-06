# Generated by Django 2.1 on 2019-07-24 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0002_auto_20190721_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='payinfo',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='收货地址'),
        ),
        migrations.AddField(
            model_name='payinfo',
            name='signer_name',
            field=models.CharField(default='', max_length=20, verbose_name='签收人'),
        ),
        migrations.AddField(
            model_name='payinfo',
            name='singer_mobile',
            field=models.CharField(default='', max_length=11, verbose_name='联系电话'),
        ),
        migrations.AlterField(
            model_name='payinfo',
            name='order_sn',
            field=models.CharField(blank=True, default='', max_length=50, null=True, unique=True, verbose_name='订单编号'),
        ),
        migrations.AlterField(
            model_name='payinfo',
            name='pay_sn',
            field=models.CharField(blank=True, default='', max_length=50, null=True, unique=True, verbose_name='支付编号'),
        ),
        migrations.AlterField(
            model_name='payinfo',
            name='status',
            field=models.CharField(choices=[('TRADE_SUCCESS', '成功'), ('TRADE_CLOSED', '超时关闭'), ('WAIT_BUYER_PAY', '交易创建'), ('TRADE_FINISHED', '交易结束'), ('paying', '待支付')], default='paying', max_length=7, verbose_name='订单状态'),
        ),
    ]
