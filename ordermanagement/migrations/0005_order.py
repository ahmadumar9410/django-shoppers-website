# Generated by Django 3.0.1 on 2020-01-04 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanagement', '0004_auto_20200104_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
            ],
        ),
    ]