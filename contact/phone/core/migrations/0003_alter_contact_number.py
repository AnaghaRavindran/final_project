# Generated by Django 4.0.6 on 2022-07-04 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_contact_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
