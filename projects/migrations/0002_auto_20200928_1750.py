# Generated by Django 3.1.1 on 2020-09-29 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='clientName',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='liveURL',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='playURL',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='repoURL',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
