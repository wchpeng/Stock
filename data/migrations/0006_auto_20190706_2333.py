# Generated by Django 2.1.7 on 2019-07-06 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20190706_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='ask1',
            field=models.FloatField(default=0.0, verbose_name='卖一价'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ask2',
            field=models.FloatField(default=0.0, verbose_name='卖二价'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ask3',
            field=models.FloatField(default=0.0, verbose_name='卖三价'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ask4',
            field=models.FloatField(default=0.0, verbose_name='卖四价'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ask5',
            field=models.FloatField(default=0.0, verbose_name='卖五价'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='bind1',
            field=models.FloatField(default=0.0, verbose_name='买一价'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='bind2',
            field=models.FloatField(default=0.0, verbose_name='买二价'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='bind3',
            field=models.FloatField(default=0.0, verbose_name='买三价'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='bind4',
            field=models.FloatField(default=0.0, verbose_name='买四价'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='bind5',
            field=models.FloatField(default=0.0, verbose_name='买五价'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='buy',
            field=models.FloatField(default=0.0, verbose_name='竞买价'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='close',
            field=models.FloatField(default=0.0, verbose_name='收盘价（昨天）'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='high',
            field=models.FloatField(default=0.0, verbose_name='今日最高价'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='low',
            field=models.FloatField(default=0.0, verbose_name='今日最低价'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='now',
            field=models.FloatField(default=0.0, verbose_name='现价'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='open',
            field=models.FloatField(default=0.0, verbose_name='开盘价'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sell',
            field=models.FloatField(default=0.0, verbose_name='竞卖价'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='ask1',
            field=models.FloatField(default=0.0, verbose_name='卖一价'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='ask2',
            field=models.FloatField(default=0.0, verbose_name='卖二价'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='ask3',
            field=models.FloatField(default=0.0, verbose_name='卖三价'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='ask4',
            field=models.FloatField(default=0.0, verbose_name='卖四价'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='ask5',
            field=models.FloatField(default=0.0, verbose_name='卖五价'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='bind1',
            field=models.FloatField(default=0.0, verbose_name='买一价'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='bind2',
            field=models.FloatField(default=0.0, verbose_name='买二价'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='bind3',
            field=models.FloatField(default=0.0, verbose_name='买三价'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='bind4',
            field=models.FloatField(default=0.0, verbose_name='买四价'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='bind5',
            field=models.FloatField(default=0.0, verbose_name='买五价'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='buy',
            field=models.FloatField(default=0.0, verbose_name='竞买价'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='high',
            field=models.FloatField(default=0.0, verbose_name='今日最高价'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='low',
            field=models.FloatField(default=0.0, verbose_name='今日最低价'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='now',
            field=models.FloatField(default=0.0, verbose_name='现价'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='sell',
            field=models.FloatField(default=0.0, verbose_name='竞卖价'),
        ),
    ]
