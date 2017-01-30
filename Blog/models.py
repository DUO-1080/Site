from django.db import models

# Create your models here.
class Artical(models.Model):
    STATUS = (
        ('D','Draft'),
        ('P','Published')
    )
    title = models.CharField('标题',max_length=50)
    body = models.TextField('正文')
    create_time = models.DateTimeField(auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS,default='D',max_length=1)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    topped = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag',verbose_name='标签',null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_time']


class Tag(models.Model):
    name = models.CharField('标签',max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user_name = models.CharField('评论者名字',max_length=10)
    body = models.TextField('评论内容')
    create_time = models.DateTimeField(auto_now_add=True)
    artical = models.ForeignKey('Artical',on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:20]



