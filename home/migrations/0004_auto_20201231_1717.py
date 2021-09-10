# Generated by Django 3.1.4 on 2020-12-31 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201231_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='id',
        ),
        migrations.AlterField(
            model_name='results',
            name='candidate',
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='votinglist',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
