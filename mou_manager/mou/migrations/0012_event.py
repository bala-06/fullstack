# Generated by Django 5.1.2 on 2025-01-06 03:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mou', '0011_mou_organization_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=50)),
                ('mou', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='mou.mou')),
            ],
        ),
    ]
