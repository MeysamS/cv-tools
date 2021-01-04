# Generated by Django 3.1.4 on 2021-01-04 08:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('slug', models.SlugField(allow_unicode=True, help_text='این فیل به صورت خودکار زمانی که عنوان را وارد میکنید پر خواهد شد', max_length=100, unique=True, verbose_name='آدرس لینک')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('thumbnail', models.ImageField(upload_to='blog', verbose_name='تصویر')),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], max_length=1, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]