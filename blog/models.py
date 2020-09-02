from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.utils.text import slugify
from django.db import models

def arabic_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str

# Create your models here.
class Category(models.Model):
    title = models.CharField(default='التصنيف',max_length=255, verbose_name="التصنيف",help_text='قم بادخال اسم التصنيف ')
    slug = models.SlugField(blank=True,null=True,unique=True,allow_unicode=True,help_text='يفضل تركه فارغا')
    class Meta:
        verbose_name = (' التصنيف')
        verbose_name_plural = ('التصنيفات ')
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='العنوان',help_text='قم بادخال عنوان المنشور')
    content = models.TextField(verbose_name='الوصف',help_text='قم بادخال الوصف')
    files = models.FileField(blank=True,null=True,upload_to='media',verbose_name='المخطط')
    title2 = models.CharField(null=True,blank=True,max_length=100,verbose_name='عنوان الرابط او الصوره',help_text='قم بادخال عنوان للرابط الذي تريد وضعه او للصوره التي تريد وضعها')
    url = models.URLField(null=True,blank=True,verbose_name='الرابط',help_text='قم بادخال الرابط ')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True,related_name='posts', verbose_name="التصنيف ",help_text='قم باختيار التصنيف')
    slug = models.SlugField(blank=True,null=True,unique=True,allow_unicode=True,help_text='يفضل تركه فارغا')
    post_date = models.DateTimeField(default=timezone.now,help_text='يفضل تركه كما هو',verbose_name='تاريخ المنشور')
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم')
    active = models.BooleanField(default=True,verbose_name='تفعيل')

    @property
    def ImageURL(self):
        try:
            url = self.files.url
        except:
            url = ''
        return url




    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(Post,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/detail/{self.slug}'

    class Meta:
        ordering = ('-post_date',)
        verbose_name = ('المنشور')
        verbose_name_plural = ('المنشورات')

class PostS(models.Model):
    title = models.CharField(max_length=100,verbose_name='العنوان',help_text='قم بادخال عنوان المنشور')
    content = models.TextField(null=True,blank=True,verbose_name='الوصف',help_text='قم بادخال الوصف')
    files = models.FileField(blank=True,null=True,upload_to='media',verbose_name='المخطط')
    url = models.URLField(null=True,blank=True,verbose_name='الرابط',help_text='قم بادخال الرابط ')
    slug = models.SlugField(blank=True,null=True,unique=True,allow_unicode=True,help_text='يفضل تركه فارغا')
    post_date = models.DateTimeField(default=timezone.now,help_text='يفضل تركه كما هو',verbose_name='تاريخ المنشور')
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم')
    active = models.BooleanField(default=True,verbose_name='تفعيل')

    @property
    def ImageURL(self):
        try:
            url = self.files.url
        except:
            url = ''
        return url




    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(PostS,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/detail/{self.slug}'

    class Meta:
        ordering = ('-post_date',)
        verbose_name = ('مخططات رفحاء المطوره')
        verbose_name_plural = ('مخططات رفحاء المطوره')

class PostSS(models.Model):
    title = models.CharField(max_length=100,verbose_name='العنوان',help_text='قم بادخال عنوان المنشور')
    content = models.TextField(null=True,blank=True,verbose_name='الوصف',help_text='قم بادخال الوصف')
    files = models.FileField(blank=True,null=True,upload_to='media',verbose_name='الصوره')
    url = models.URLField(null=True,blank=True,verbose_name='الرابط',help_text='قم بادخال الرابط ')
    slug = models.SlugField(blank=True,null=True,unique=True,allow_unicode=True,help_text='يفضل تركه فارغا')
    post_date = models.DateTimeField(default=timezone.now,help_text='يفضل تركه كما هو',verbose_name='تاريخ المنشور')
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='المستخدم')
    active = models.BooleanField(default=True,verbose_name='تفعيل')

    @property
    def ImageURL(self):
        try:
            url = self.files.url
        except:
            url = ''
        return url




    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(PostSS,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/detail/{self.slug}'

    class Meta:
        ordering = ('-post_date',)
        verbose_name = (' سياره ')
        verbose_name_plural = ('  سيارات')



