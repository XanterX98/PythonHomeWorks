# Generated by Django 4.0.6 on 2022-08-02 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_alter_teacher_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
    ]
