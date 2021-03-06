# Generated by Django 2.2.6 on 2021-06-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producer', models.CharField(max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('series_date', models.IntegerField(max_length=4)),
                ('transmission', models.SmallIntegerField(choices=[(1, 'Manual'), (2, 'Automatic'), (3, 'Robotic')])),
                ('color', models.CharField(max_length=64)),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]
