# Generated by Django 2.2.4 on 2019-08-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20190812_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attend',
            name='attend_status',
            field=models.CharField(choices=[('출석가능', '출석가능'), ('출석불가', '출석불가')], default='출석불가', max_length=15),
        ),
    ]
