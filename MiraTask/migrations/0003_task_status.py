# Generated by Django 3.2.6 on 2021-08-31 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiraTask', '0002_alter_task_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TODO', 'to-do'), ('DOING', 'doing'), ('DONE', 'done')], default='TODO', max_length=5),
        ),
    ]