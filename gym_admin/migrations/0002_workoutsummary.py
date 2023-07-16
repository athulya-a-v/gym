# Generated by Django 4.2.1 on 2023-06-24 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_type', models.CharField(max_length=100)),
                ('days_per_week', models.CharField(max_length=100)),
                ('time_per_workout', models.CharField(max_length=100)),
                ('equipment_required', models.CharField(max_length=100)),
                ('target_gender', models.CharField(max_length=20)),
                ('createplan_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_admin.createplan')),
            ],
        ),
    ]
