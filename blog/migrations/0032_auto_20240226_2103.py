# Generated by Django 3.2 on 2024-02-26 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20240226_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='breadcrumb',
            field=models.CharField(blank=True, max_length=156, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='canonical',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='description',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='h1',
            field=models.CharField(blank=True, max_length=156, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='SEO'),
        ),
        migrations.AddField(
            model_name='place',
            name='keyword',
            field=models.CharField(blank=True, max_length=156, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='og_card',
            field=models.CharField(blank=True, max_length=156, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='og_site',
            field=models.CharField(blank=True, max_length=156, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='og_type',
            field=models.CharField(blank=True, max_length=156, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.CharField(blank=True, max_length=1256, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='title',
            field=models.CharField(blank=True, max_length=156, null=True),
        ),
    ]
