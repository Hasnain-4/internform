# Generated by Django 3.0.6 on 2020-11-19 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0002_auto_20201119_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='type_env',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='type_inju',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='type_property',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='type_vehicle',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]