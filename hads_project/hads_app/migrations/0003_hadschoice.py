# Generated by Django 4.2.3 on 2023-07-28 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hads_app', '0002_hadsquestion_subscale_hadsquestion_weight_0_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HADSChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')])),
                ('text', models.CharField(max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='hads_app.hadsquestion')),
            ],
        ),
    ]