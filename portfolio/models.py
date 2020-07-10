
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Portfolio(models.Model):
    
    project_name = models.CharField(max_length = 50,verbose_name = "Name")
    project_description = models.CharField(max_length = 200,verbose_name = "Description")
    project_content=models.TextField(verbose_name = "Content")
    comment_date = models.DateTimeField(auto_now_add=True)
    project_image = models.FileField(blank = True,null = True,verbose_name=" Add p Image")

    def __str__(self):
        return self.project_name
    