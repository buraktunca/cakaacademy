# Generated by Django 3.0.7 on 2022-09-02 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dersler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ders_adi', models.CharField(max_length=360)),
                ('ders_tipi', models.CharField(choices=[('TYT', 'TYT'), ('AYT', 'AYT')], max_length=3)),
                ('upload_date', models.DateField()),
                ('ders_konu', models.CharField(max_length=360)),
            ],
        ),
    ]
