# Generated by Django 3.2.12 on 2022-08-05 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('price', models.FloatField(default=50.0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('expired_on', models.DateTimeField(blank=True, null=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.book')),
            ],
            options={
                'db_table': 'management_rent',
            },
        ),
    ]
