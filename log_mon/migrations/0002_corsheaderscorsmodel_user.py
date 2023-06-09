# Generated by Django 4.1.1 on 2022-10-28 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_mon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorsheadersCorsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cors', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'corsheaders_corsmodel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=45, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('hashed_password', models.TextField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
