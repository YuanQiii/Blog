from django.db import models


# Create your models here.
class SayName(models.Model):
    firstName = models.CharField(max_length=16)
    lastName = models.CharField(max_length=16)


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='标题')
    tag = models.CharField(max_length=16, verbose_name='标签')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    description = models.CharField(max_length=32, default='嘿嘿', verbose_name='描述')
    count = models.IntegerField(default=0, verbose_name='流量统计')

    class Meta:
        verbose_name = verbose_name_plural = '文章'


class ArticleContent(models.Model):
    sub_title = models.CharField(max_length=16, verbose_name='次级标题')
    content = models.CharField(max_length=4096, verbose_name='内容')
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE, verbose_name='主标题', default='')


    class Meta:
        verbose_name = verbose_name_plural = '内容'


class Comment(models.Model):
    name = models.CharField(max_length=32, verbose_name='昵称')
    comment = models.CharField(max_length=128, verbose_name='内容')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    class Meta:
        verbose_name = verbose_name_plural = '评论'


class Archives(models.Model):
    title = models.CharField(max_length=32, default='title')
    content = models.CharField(max_length=1024, default='content')
    createTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '归档'
        ordering = ['-id']


class Opinion(models.Model):
    name = models.CharField(max_length=32, default='')
    content = models.CharField(max_length=256, default='')
    createTime = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(to='Article', on_delete=models.CASCADE, null=True, blank=True)
