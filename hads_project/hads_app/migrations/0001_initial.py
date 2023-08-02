# Generated by Django 4.2.3 on 2023-07-28 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HADSQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HADSTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anxiety_scores', models.IntegerField(default=0)),
                ('depression_scores', models.IntegerField(default=0)),
                ('date_completed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]