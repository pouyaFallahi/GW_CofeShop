# Generated by Django 5.0 on 2023-12-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffe', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='myuser',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='myuser',
            name='gender',
            field=models.CharField(choices=[('F', 'زن'), ('M', 'مرد'), ('o', 'متفرقه')], max_length=1),
        ),
    ]
