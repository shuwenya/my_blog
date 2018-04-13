from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    """
    分类
    """
    name = models.CharField(u'分类', max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(u'标签', max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):

    # 文章标题
    title = models.CharField(u'标题', max_length=70)

    # 文章正文，我们使用了 TextField。
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField(u'正文')

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField(u'创建时间')
    modified_time = models.DateTimeField(u'修改时间')

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(u'摘要', max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        path = reverse('article:detail', kwargs={'my_args' : self.id})
        return "http://127.0.0.1:8000%s" % path

    class Meta:
        ordering = ['-created_time']