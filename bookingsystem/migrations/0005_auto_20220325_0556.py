# Generated by Django 3.2 on 2022-03-25 05:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookingsystem', '0004_auto_20220324_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('number_of_guests', models.IntegerField(default=1)),
                ('check_in_date', models.DateField(default=datetime.date.today)),
                ('number_of_nights', models.IntegerField(default=1)),
                ('type_of_room', models.CharField(choices=[('Single', 'Single Room'), ('Double', 'Double Room'), ('Family', 'Family Room')], default='Single', max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bookings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['check_in_date'],
            },
        ),
        migrations.DeleteModel(
            name='Bookings',
        ),
    ]
