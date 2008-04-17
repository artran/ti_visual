from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return 'Message from %s (%s) - %s' % (self.name, self.email, self.message)
    class Admin:
        pass