# Generated by Django 3.2.7 on 2021-11-28 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor', models.IntegerField(default=None)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.post')),
            ],
        ),
    ]
