from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=50)
    # description=models.TextField(verbose_name='description',blank=True)
    # content=models.TextField(verbose_name='content')
   
    created_date=models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank = True,null = True,verbose_name=" Add Image")
    
    content = RichTextField()
    

    def __str__(self):
        return self.title
    def get_image_path(self):
        return 'img/'+self.image

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "Name")
    comment_content = models.CharField(max_length = 200,verbose_name = "Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content

class Portfolio(models.Model):
    
    project_name = models.CharField(max_length = 50,verbose_name = "Name")
    project_description = models.CharField(max_length = 200,verbose_name = "Description")
    project_content=models.TextField(verbose_name = "Content")
    comment_date = models.DateTimeField(auto_now_add=True)
    project_image = models.FileField(blank = True,null = True,verbose_name=" Add Image")

    def __str__(self):
        return self.project_name
    
    

