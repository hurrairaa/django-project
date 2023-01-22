from django.db import models

# Create your models here.
class Blog(models.Model):  
    title = models.CharField(max_length=100)  
    description = models.CharField(max_length=1000)  
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:  
        db_table = "blogs"  