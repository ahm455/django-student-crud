from django.db import models

class student(models.Model):
    name= models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    age=models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    


