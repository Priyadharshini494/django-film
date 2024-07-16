from django.db import models 

class BaseModel(models.Model):
    last_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True