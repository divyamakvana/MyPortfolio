from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text="Technologies used, comma separated")
   
    
    github_link = models.CharField(max_length=50, default=False)
    date_completed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp1


class Certificate(models.Model):
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200) 
    date_earned = models.DateField()
    certificate_link = models.URLField()

    def __str__(self):
        return self.title