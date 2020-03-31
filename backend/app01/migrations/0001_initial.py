# Generated by Django 3.0 on 2020-03-29 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=32)),
                ('content', models.CharField(default='content', max_length=1024)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '归档',
                'verbose_name_plural': '归档',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('tag', models.CharField(max_length=16, verbose_name='标签')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('description', models.CharField(default='嘿嘿', max_length=32, verbose_name='描述')),
                ('count', models.IntegerField(default=0, verbose_name='流量统计')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='昵称')),
                ('comment', models.CharField(max_length=128, verbose_name='内容')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='SayName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=16)),
                ('lastName', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=32)),
                ('content', models.CharField(default='', max_length=256)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Article')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=16, verbose_name='次级标题')),
                ('content', models.CharField(max_length=2048, verbose_name='内容')),
                ('article', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app01.Article', verbose_name='主标题')),
            ],
            options={
                'verbose_name': '内容',
                'verbose_name_plural': '内容',
            },
        ),
    ]