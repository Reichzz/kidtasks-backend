# Generated by Django 5.0.4 on 2024-07-31 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidtasks', '0003_alter_task_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
