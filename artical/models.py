from django.db import models
from DjangoUeditor.models import UEditorField
import datetime
from django.contrib.auth.models import User,Group

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=20,verbose_name='名称',help_text='大类')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = '新闻类别'
        verbose_name_plural = verbose_name


class Item(models.Model):
    title = models.CharField(max_length=20,verbose_name='名称',help_text='名称')
    create_date = models.DateTimeField(default=datetime.datetime.now(),verbose_name='创建时间',help_text='创建时间')
    completed = models.BooleanField(default=False,verbose_name='是否完成',help_text='是否完成')
    categorys = models.ForeignKey(Category,related_name='item_category',on_delete=models.CASCADE,help_text='大类')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = '新闻子栏目'
        verbose_name_plural = verbose_name

class Tag(models.Model):
    name = models.CharField(max_length=50,verbose_name='名称',help_text='名称')
    slug = models.SlugField(max_length=50,verbose_name='描述')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '标签'
        verbose_name_plural = verbose_name

class Artical(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题',help_text='标题')
    slug = models.SlugField(unique_for_year='',verbose_name='描述')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='artical_author',verbose_name='作者',help_text='作者')
    content = UEditorField('内容',height=400,width=600,default='',imagePath='upload/',toolbars='mini',filePath='upload/',blank=True)
