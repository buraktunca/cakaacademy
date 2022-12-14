# Generated by Django 3.0.7 on 2022-09-06 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_auto_20220905_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='testler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_seviyesi', models.CharField(choices=[('Kolay', 'Kolay'), ('Orta', 'Orta'), ('Zor', 'Zor')], default='Orta', max_length=30)),
                ('test_tipi', models.CharField(choices=[('TYT', 'TYT'), ('AYT', 'AYT')], max_length=3)),
                ('test_adi', models.CharField(max_length=360)),
                ('ders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Dersler')),
            ],
        ),
        migrations.CreateModel(
            name='test_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_question', models.ImageField(upload_to='test_questions/')),
                ('right_answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.testler')),
            ],
        ),
        migrations.CreateModel(
            name='test_answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1)),
                ('test_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.test_questions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
