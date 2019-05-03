# Generated by Django 2.1.7 on 2019-05-03 08:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_now', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.CharField(max_length=50)),
                ('do_exercises', models.BooleanField(default=True)),
                ('scale', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default=('1', '1'), max_length=2)),
            ],
        ),
    ]
