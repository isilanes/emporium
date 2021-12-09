# Generated by Django 3.2.7 on 2021-12-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaseTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('path', models.FileField(upload_to='leases/templates')),
            ],
        ),
    ]
