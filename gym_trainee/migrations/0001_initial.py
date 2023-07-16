# Generated by Django 4.2.1 on 2023-07-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TraineeRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainee_addrress', models.TextField()),
                ('trainee_pincode', models.BigIntegerField()),
                ('trainee_state', models.CharField(default='', max_length=30)),
                ('trainee_city', models.CharField(default='', max_length=30)),
                ('trainee_gender', models.CharField(default='', max_length=8)),
                ('trainee_dob', models.DateField()),
                ('register_phone', models.BigIntegerField()),
            ],
        ),
    ]
