# Generated by Django 2.2 on 2019-04-05 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amenities_list', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Stars', models.IntegerField()),
                ('Type', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Key_Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Trip_Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('Night', models.IntegerField()),
                ('Day', models.IntegerField()),
                ('Cost', models.IntegerField()),
                ('Cities', models.ManyToManyField(to='package.City')),
                ('Keys', models.ManyToManyField(to='package.Key_Features')),
            ],
        ),
        migrations.CreateModel(
            name='Trip_Origin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.City')),
                ('Package_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='package.Trip_Package')),
            ],
        ),
        migrations.CreateModel(
            name='Trip_Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.City')),
                ('Package_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='package.Trip_Package')),
            ],
        ),
        migrations.CreateModel(
            name='Total_Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity', models.CharField(max_length=15)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Price_Per_Person', models.IntegerField()),
                ('Duration', models.IntegerField()),
                ('Sutaible_For', models.CharField(max_length=5)),
                ('Transport_Mode', models.CharField(max_length=15)),
                ('City_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.City')),
            ],
        ),
        migrations.CreateModel(
            name='Price_Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Per_Day', models.IntegerField()),
                ('Hotel_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Package_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.IntegerField()),
                ('Title', models.CharField(max_length=25)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Activities', models.ManyToManyField(to='package.Total_Activities')),
                ('City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.City')),
                ('Hotel_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.Hotel')),
                ('Package_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.Trip_Package')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Street_1', models.CharField(max_length=100)),
                ('Street_2', models.CharField(max_length=100)),
                ('City_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.City')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='Address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.Hotel_Address'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='Amenities_List',
            field=models.ManyToManyField(to='package.Amenities'),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='photos')),
                ('Activity_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.Total_Activities')),
            ],
        ),
        migrations.CreateModel(
            name='Extra_Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.Total_Activities')),
                ('Booking_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.Trip_Package')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adults', models.IntegerField()),
                ('Child', models.IntegerField()),
                ('Infant', models.IntegerField()),
                ('Fare', models.IntegerField()),
                ('Package_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.Trip_Package')),
                ('User_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
