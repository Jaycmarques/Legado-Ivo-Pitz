# Generated by Django 5.0.6 on 2024-08-29 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_css_file_page_redirect_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='css_file',
        ),
        migrations.AddField(
            model_name='page',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='page_images/'),
        ),
    ]
