from django.db import models
from .user import User

class Group(models.Model):
    id_group = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 80, null = False)
    type = models.CharField(max_length = 3 ,null = False, blank = False)
    dt_created = models.DateTimeField(auto_now_add = True)
    id_user = models.ManyToManyField(User)

    def __str__(self):
        user = [id_users for id_users["id_user"] in self.id_user.values()]
        return f"""
            id_group: {self.id_group},\n 
            name: {self.name},\n 
            type: {self.name}, \n
            users: {user}\n
            dt_created: {self.dt_created}
            """

            
        