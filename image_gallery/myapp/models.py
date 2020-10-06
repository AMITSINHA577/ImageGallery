from django.db import models


# Create your models here.

#create categories model
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.title

# create Image model
class Image(models.Model):
    title=models.CharField(max_length=200)
    description = models.TextField()
    image=models.ImageField(upload_to='images')
    added_date=models.DateTimeField()
    cat=models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title




class LoginDetails(models.Model):
    name = models.CharField(max_length=50)
    emailid = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name