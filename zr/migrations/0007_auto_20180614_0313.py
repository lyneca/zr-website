# Generated by Django 2.0 on 2018-06-14 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zr', '0006_auto_20180614_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zr.Answer'),
        ),
    ]
