# Generated by Django 5.0.6 on 2025-01-25 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familytree', '0004_remove_familymember_divorced_parent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dedicatoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('message', models.TextField(verbose_name='Mensagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Envio')),
                ('is_published', models.BooleanField(default=False, verbose_name='Publicado?')),
            ],
        ),
        migrations.AlterField(
            model_name='familymember',
            name='info',
            field=models.TextField(blank=True, db_index=True, max_length=1000, null=True),
        ),
    ]
