# Generated by Django 3.1.4 on 2021-01-02 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='educations',
            options={'verbose_name_plural': 'تحصیلات'},
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatar'),
        ),
    ]
