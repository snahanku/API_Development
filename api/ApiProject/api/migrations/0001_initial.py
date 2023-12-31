# Generated by Django 4.1.3 on 2023-07-02 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=1000)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobile phones', 'Mobile phones')], max_length=100)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
