# Generated by Django 2.0 on 2018-06-13 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Question')),
                ('answer', models.TextField(verbose_name='Answer')),
                ('answerer', models.TextField(verbose_name='Answerer')),
                ('submitter', models.TextField(verbose_name='Submitter')),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name='Date submitted')),
            ],
        ),
    ]
