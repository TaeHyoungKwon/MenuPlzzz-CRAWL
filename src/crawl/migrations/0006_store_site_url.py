# Generated by Django 2.1.7 on 2019-06-14 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0005_store_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='site_url',
            field=models.CharField(max_length=200, null=True, verbose_name='사이트 URL'),
        ),
    ]