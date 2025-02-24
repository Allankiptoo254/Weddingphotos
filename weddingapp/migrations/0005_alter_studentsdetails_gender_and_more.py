# Generated by Django 5.0.3 on 2024-07-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingapp', '0004_studentsdetails_alter_studentsmodel_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsdetails',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=18),
        ),
        migrations.AlterField(
            model_name='studentsdetails',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
