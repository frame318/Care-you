# Generated by Django 3.2.7 on 2021-12-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeDrug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_drug', models.TimeField()),
                ('text_drug', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RemindersDrug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255, unique=True)),
                ('reminders_user', models.TextField(blank=True)),
                ('time_drug', models.ManyToManyField(blank=True, to='liff.TimeDrug')),
            ],
        ),
    ]
