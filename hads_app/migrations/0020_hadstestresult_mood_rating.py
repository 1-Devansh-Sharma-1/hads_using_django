# Generated by Django 4.2.3 on 2023-08-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hads_app', '0019_remove_subjectiveresponse_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='hadstestresult',
            name='mood_rating',
            field=models.IntegerField(default=0),
        ),
    ]
