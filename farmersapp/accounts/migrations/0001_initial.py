# Generated by Django 2.2 on 2019-04-10 12:41

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('officer', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Parish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.AutoField(choices=[('2018A', '2018A'), ('2018B', '2018B'), ('2018C', '2018C')], primary_key=True, serialize=False)),
                ('area', models.IntegerField(verbose_name='eg 2ac')),
                ('harvest', models.IntegerField(verbose_name='eg 5000kg')),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='village name', max_length=40)),
                ('parish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Parish')),
            ],
        ),
        migrations.CreateModel(
            name='Subcounty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.District')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_area', models.CharField(choices=[('2.0 AC', '1-5 AC'), ('2.0 AC', '2.0 AC')], max_length=20)),
                ('rice_type', models.CharField(choices=[('K', 'Kaiso'), ('S', 'Super'), ('T', 'Tilda')], max_length=1)),
                ('sowing_type', models.CharField(max_length=100)),
                ('planting_type', models.CharField(max_length=100)),
                ('levelling', models.CharField(choices=[('B', 'Bad'), ('F', 'Fair'), ('G', 'Good')], max_length=1)),
                ('rigde', models.CharField(choices=[('B', 'Bad'), ('F', 'Fair'), ('G', 'Good')], max_length=1)),
                ('watercourse_state', models.CharField(choices=[('B', 'Bad'), ('F', 'Fair'), ('G', 'Good')], max_length=1)),
                ('fertilizer', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('fertilizer_1_type', models.CharField(max_length=80)),
                ('fertilizer_1_amount', models.IntegerField()),
                ('fertilizer_2_type', models.CharField(max_length=80)),
                ('fertilizer_2_amount', models.IntegerField()),
                ('weed_condition', models.CharField(choices=[('B', 'Bad'), ('F', 'Fair'), ('G', 'Good')], max_length=1)),
                ('harvest_date', models.DateField()),
                ('session_id', models.ForeignKey(choices=[('2018A', '2018A'), ('2018B', '2018B'), ('2018C', '2018C')], on_delete=django.db.models.deletion.CASCADE, to='accounts.Session')),
            ],
        ),
        migrations.AddField(
            model_name='parish',
            name='sub_county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Subcounty'),
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your full name', max_length=40)),
                ('login_id', models.CharField(help_text='Unique ID for every officer', max_length=255, unique=True)),
                ('password', models.CharField(max_length=8)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.District')),
                ('subcounty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Subcounty')),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='enter your full name', max_length=40)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birth_year', models.DateField(help_text='date of birth')),
                ('marriage', models.CharField(blank=True, choices=[('M', 'Married'), ('S', 'Single'), ('D', 'Divorced')], max_length=1)),
                ('language', models.CharField(blank=True, choices=[('LUGANDA', 'Luganda'), ('LUSOGA', 'Lusoga'), ('ACHOLI', 'Acholi'), ('RUNYANKOLE', 'Runyankole')], max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('photo', models.FileField(upload_to='images/')),
                ('community_status', models.CharField(blank=True, choices=[('MOBILIZER', 'Mobilizer'), ('CHAIRMAN', 'Chairman'), ('OTHER_ROLES', 'Other_roles')], max_length=60)),
                ('instructor_possibility', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('crop_type', models.CharField(choices=[('POTATO', 'Potato'), ('MAIZE', 'Maize'), ('BEANS', 'Bean'), ('RICE', 'Rice')], max_length=40)),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.District')),
                ('parish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Parish')),
                ('subcounty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Subcounty')),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Village')),
            ],
        ),
    ]
