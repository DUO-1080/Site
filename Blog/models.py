from django.db import models

# Create your models here.
class Artical(models.Model):
    STATUS = (
        ('D','Draft'),
        ('P','Published')
    )
    title = models.CharField('标题',max_length=50)
    body = models.TextField('正文')
    creat_time = models.DateTimeField(auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS,default='D',max_length=1)
    abstract = models.CharField(max_length=200,blank=True,null=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    topped = models.BooleanField(default=False)
    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']


class Category(models.Model):
    name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

