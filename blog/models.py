from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateField()
    image = models.ImageField(upload_to="images/", blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts", null=True)

    def __str__(self):
        return self.title




# from django.db import models

# # Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     description =models.TextField()
#     date_posted = models.DateField()
#     image = models.ImageField(upload_to="static/img/", blank=True)

#     def __str__(self):
#         return self.title