# Generated by Django 4.2.4 on 2023-12-28 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_sub_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_available',
            new_name='isAvailable',
        ),
        migrations.AddField(
            model_name='product',
            name='modals',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='star',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
