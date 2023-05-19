# Generated by Django 2.2 on 2023-05-19 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gene', '0008_auto_20230517_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='BDNF_gene',
            field=models.IntegerField(choices=[(1, 'AA'), (2, 'AG'), (3, 'GG')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='FTO_gene',
            field=models.IntegerField(choices=[(1, 'TT'), (2, 'TA'), (3, 'AA')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='MC4R_gene',
            field=models.IntegerField(choices=[(1, 'TT'), (2, 'TC'), (3, 'CC')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='diary',
            name='feeling_rating',
            field=models.IntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default=None),
        ),
    ]
