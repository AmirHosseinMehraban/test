# Generated by Django 4.2.4 on 2023-12-29 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='verification_code',
            new_name='verificationCode',
        ),
    ]