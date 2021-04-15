# Generated by Django 3.1.7 on 2021-04-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
