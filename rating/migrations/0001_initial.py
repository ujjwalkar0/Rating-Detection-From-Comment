# Generated by Django 4.1 on 2022-08-26 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RatingReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=None)),
                ('que_1', models.TextField(default=None)),
                ('que_2', models.TextField(default=None)),
                ('que_3', models.TextField(default=None)),
                ('que_4', models.TextField(default=None)),
                ('que_5', models.TextField(default=None)),
                ('rating', models.IntegerField(default=None)),
            ],
        ),
    ]