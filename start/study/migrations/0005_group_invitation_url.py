# Generated by Django 2.2.4 on 2019-08-06 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_group_group_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='invitation_url',
            field=models.CharField(default='', max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
