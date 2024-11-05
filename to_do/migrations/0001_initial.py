# Generated by Django 5.1 on 2024-11-04 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('created_Date', models.DateTimeField(auto_now_add=True)),
                ('updated_Date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('not_started', 'Not Started'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('on_hold', 'On Hold')], default='Not Started', max_length=20)),
            ],
        ),
    ]
