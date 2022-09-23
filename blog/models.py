from django.db import models

# Create your models here.
class Category(models.Model):  #blog_category
    category = models.CharField(max_length = 100)

    def __str__(self):
        return self.category;


class Blog(models.Model): #blog_blog
    title = models.CharField(max_length=100)
    post = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)


    def __str__(self):
        return self.title