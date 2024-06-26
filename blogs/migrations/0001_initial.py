# Generated by Django 5.0.6 on 2024-05-15 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_blog', models.CharField(max_length=200)),
                ('pages', models.IntegerField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.authors')),
            ],
        ),
    ]
