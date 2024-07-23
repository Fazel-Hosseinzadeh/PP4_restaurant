from django.db import models


class ContactContent(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class ContactMessage(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"