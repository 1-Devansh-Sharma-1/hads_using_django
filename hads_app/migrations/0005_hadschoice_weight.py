# Generated by Django 4.2.3 on 2023-07-28 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hads_app', '0004_remove_hadsquestion_weight_0_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hadschoice',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]