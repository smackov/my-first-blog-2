# Generated by Django 3.0.5 on 2020-07-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]
