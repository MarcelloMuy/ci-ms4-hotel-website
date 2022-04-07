# Generated by Django 3.2 on 2022-04-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsystem', '0005_auto_20220325_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='number_of_guests',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='number_of_nights',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='type_of_room',
            field=models.CharField(choices=[('Twin', 'Twin Room'), ('Double', 'Double Room'), ('Family', 'Family Room')], default='Double', max_length=15),
        ),
        migrations.AddConstraint(
            model_name='booking',
            constraint=models.CheckConstraint(check=models.Q(number_of_guests__range=(1, 10)), name='bookingsystem_booking_number_of_guests__range'),
        ),
    ]
