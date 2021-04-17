from django.db import models

class Group(models.Model):
    id_group = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 80)
    dt_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"""
            id_group: {self.id_group},\n 
            name: {self.name},\n 
            dt_created: {self.dt_created}
            """

            
        