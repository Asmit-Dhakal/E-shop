# Generated by Django 4.2.4 on 2023-09-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_rename_phonenumber_contact_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='citizenship',
            field=models.ImageField(default='0', upload_to=''),
        ),
    ]
