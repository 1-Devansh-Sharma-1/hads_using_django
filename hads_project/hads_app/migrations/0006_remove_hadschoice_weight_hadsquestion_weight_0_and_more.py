# Generated by Django 4.2.3 on 2023-07-28 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hads_app', '0005_hadschoice_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hadschoice',
            name='weight',
        ),
        migrations.AddField(
            model_name='hadsquestion',
            name='weight_0',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hadsquestion',
            name='weight_1',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='hadsquestion',
            name='weight_2',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='hadsquestion',
            name='weight_3',
            field=models.IntegerField(default=3),
        ),
    ]
