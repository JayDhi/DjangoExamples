# Generated by Django 2.0.3 on 2019-05-02 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20190502_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 2, 11, 46, 13, 41004), help_text='发布日期', verbose_name='发布日期'),
        ),
    ]
