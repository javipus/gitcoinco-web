# Generated by Django 2.1.5 on 2019-03-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_refundfeerequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refundfeerequest',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='refundfeerequest',
            name='txnId',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]