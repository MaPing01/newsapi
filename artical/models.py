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
    created_date = models.DateTimeField(default=datetime.datetime.now(),verbose_name='创建时间',help_text='创建时间')
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
    status = models.CharField(max_length=2,verbose_name='状态',help_text='状态')
    tags = models.ForeignKey(Tag,related_name='artical_tags',on_delete=models.CASCADE,blank=True,help_text='文章状态')
    publish_date = models.DateTimeField(default=datetime.datetime.now(),verbose_name='发布日期',help_text='发布日期')
    expiration_date = models.DateTimeField(blank=True,null=True,verbose_name='有效日期',help_text='有效日期')
    is_activate = models.BooleanField(default=True,blank=True,verbose_name='是否热门',help_text='是否热门')
    item = models.ForeignKey(Item,related_name='artical_item',on_delete=models.CASCADE,verbose_name='',help_text='')
    picture = models.ImageField(upload_to='upload',verbose_name='图片',help_text='图片')
    praise_num = models.IntegerField(default=0,verbose_name='点赞数',help_text='点赞数')
    read_num = models.IntegerField(default=0,verbose_name='浏览数',help_text='浏览数')
    fav_num = models.IntegerField(default=0,verbose_name='收藏数',help_text='收藏数')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

class Ad(models.Model):
    title = models.CharField(max_length=50,verbose_name='',help_text='')
    pic = models.ImageField(upload_to='upload',verbose_name='',help_text='')
    adurl = models.URLField(verbose_name='',help_text='')
    adlocation = models.CharField(max_length=2,verbose_name='位置',help_text='位置')
    status = models.CharField(max_length=1,default=1,verbose_name='状态',help_text='状态')

class UserFav(models.Model):
    user = models.ForeignKey(User,related_name='fav_user',on_delete=models.CASCADE,verbose_name='用户')
    articals = models.ForeignKey(Artical,related_name='fav_artical',on_delete=models.CASCADE,verbose_name='文章')
    add_time = models.DateTimeField(default=datetime.datetime.now(),verbose_name='添加时间',help_text='添加时间')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ('user','articals')
