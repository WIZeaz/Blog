# Generated by Django 2.2 on 2019-05-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20, verbose_name='图片标题')),
                ('path', models.ImageField(default='upload/default.jpg', upload_to='upload/%Y/%m', verbose_name='图片')),
            ],
            options={
                'verbose_name': '网站相册',
                'verbose_name_plural': '网站相册',
            },
        ),
    ]
