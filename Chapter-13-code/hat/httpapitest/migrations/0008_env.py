# Generated by Django 2.2.2 on 2019-07-24 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('httpapitest', '0007_testreports'),
    ]

    operations = [
        migrations.CreateModel(
            name='Env',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('env_name', models.CharField(max_length=40, unique=True)),
                ('base_url', models.CharField(max_length=40)),
                ('simple_desc', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '环境管理',
                'db_table': 'EnvInfo',
            },
        ),
    ]