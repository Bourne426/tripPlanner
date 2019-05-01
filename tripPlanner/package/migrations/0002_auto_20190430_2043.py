# Generated by Django 2.2 on 2019-04-30 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Fare',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='User_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='extra_activity',
            name='Booking_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.Booking'),
        ),
        migrations.CreateModel(
            name='Coustomize_package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Days', models.IntegerField()),
                ('Budget', models.IntegerField()),
                ('Cities', models.ManyToManyField(to='package.City')),
                ('Keys', models.ManyToManyField(to='package.Key_Features')),
            ],
        ),
    ]
