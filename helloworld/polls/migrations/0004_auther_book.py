# Generated by Django 2.1.3 on 2019-06-26 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20190625_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auther',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='作者')),
                ('mail', models.CharField(max_length=20, verbose_name='邮箱')),
                ('city', models.CharField(max_length=10, verbose_name='城市')),
            ],
            options={
                'verbose_name_plural': '作者',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50, verbose_name='书名')),
                ('auth', models.ManyToManyField(to='polls.Auther', verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '书籍详情',
            },
        ),
    ]
