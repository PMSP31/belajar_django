# Generated by Django 3.2 on 2022-04-20 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=50)),
                ('jenis_kelamin', models.CharField(choices=[('L', 'Laki-Laki'), ('P', 'Perempuan')], max_length=1)),
                ('tanggal_lahir', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('sign_in', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
