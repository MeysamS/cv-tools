# Generated by Django 3.1.4 on 2021-01-03 13:23

from django.db import migrations, models
import extensions.validator_files


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_auto_20210103_0254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coding_skills',
            options={'verbose_name_plural': 'مهارت های کدنویسی'},
        ),
        migrations.AlterModelOptions(
            name='design_skills',
            options={'verbose_name_plural': 'مهارت های طراحی'},
        ),
        migrations.AlterModelOptions(
            name='experiences',
            options={'verbose_name_plural': 'تجربیات'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'پروفایل'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name_plural': 'کارهایی که انجام میدهم'},
        ),
        migrations.AddField(
            model_name='profile',
            name='resume_file',
            field=models.FileField(null=True, upload_to='resumeFile', validators=[extensions.validator_files.validate_file_extension]),
        ),
    ]