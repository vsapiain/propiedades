from django.db import models

class usuario_manager(models.Manager):
    
    def get_all(self):
        return self.query.all()


