# Generated by Django 4.2.11 on 2024-04-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('middle_name', models.CharField(max_length=200, null=True)),
                ('grade', models.CharField(choices=[('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=200, null=True)),
            ],
        ),
    ]
