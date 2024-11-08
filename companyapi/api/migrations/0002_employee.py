# Generated by Django 5.1.2 on 2024-10-24 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('phone', models.CharField(max_length=50)),
                ('position', models.CharField(choices=[('Manager', 'manager'), ('Software developer', 'sd'), ('Tester', 'tt')], max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]
