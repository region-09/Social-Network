# Generated by Django 4.2.6 on 2023-11-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_profileinfo_name_remove_profileinfo_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileinfo',
            name='profile_image',
            field=models.FileField(blank=True, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', null=True, upload_to='media/profile_images/'),
        ),
    ]
