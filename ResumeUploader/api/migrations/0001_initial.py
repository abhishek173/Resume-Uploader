# Generated by Django 5.1.1 on 2024-09-03 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('state', models.CharField(choices=[('bihar', 'Bihar'), ('Jharkhand', 'Jharlhand'), ('karnataka', 'Karnataka')], max_length=50)),
                ('gender', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pimage', models.ImageField(blank=True, upload_to='pimages')),
                ('rdocs', models.FileField(blank=True, upload_to='rdocs')),
            ],
        ),
    ]
