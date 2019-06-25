# Generated by Django 2.1.3 on 2019-06-25 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=50, verbose_name='银行名称')),
                ('city', models.CharField(max_length=30, verbose_name='城市')),
                ('point', models.CharField(max_length=60, verbose_name='网点')),
            ],
            options={
                'verbose_name_plural': '银行卡',
            },
        ),
        migrations.CreateModel(
            name='CardInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=30, verbose_name='卡号')),
                ('card_name', models.CharField(max_length=10, verbose_name='姓名')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Bank', verbose_name='选择银行')),
            ],
            options={
                'verbose_name_plural': '卡号信息',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': '文章列表'},
        ),
        migrations.AlterField(
            model_name='article',
            name='auth',
            field=models.CharField(max_length=10, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=30, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='最后更新时间'),
        ),
    ]
