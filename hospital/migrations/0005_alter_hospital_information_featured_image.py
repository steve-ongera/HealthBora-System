# Generated by Django 5.1.2 on 2024-11-09 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_alter_user_login_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital_information',
            name='featured_image',
            field=models.ImageField(blank=True, default='hospitals/profile.png', null=True, upload_to='hospitals/'),
        ),
    ]
