from django.db import models
from django.utils.text import slugify


class BlogCategory(models.Model):
    category = models.CharField(max_length=90, unique=True)
    
    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name_plural = "Blog Categories"

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog_category')
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='blog_images/')
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.title)
       super().save(*args, **kwargs) 
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    

