# Generated by Django 3.0.8 on 2020-09-08 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200908_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Unlike', 'Unlike'), ('Like', 'Like')], max_length=8),
        ),
    ]
