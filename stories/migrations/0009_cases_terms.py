# Generated by Django 2.2.7 on 2019-11-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0008_remove_teacher_studies'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='terms',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
