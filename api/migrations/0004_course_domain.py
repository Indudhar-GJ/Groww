# Generated by Django 5.0.4 on 2024-06-24 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_courses_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='domain',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
