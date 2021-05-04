from django.db import models
from .user import User
from .group import Group

class Historic(models.Model):
    id_message = models.AutoField(primary_key = True)
    id_user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name = "pk_hist_id_user")
    id_group = models.ForeignKey(Group, on_delete=models.RESTRICT, related_name = "pk_hist_id_group")
    content = models.TextField(null = False, blank = False)
    link = models.TextField()
    dt_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        user = self.id_user
        group = self.id_group
        return f"""
            id_message : {self.id_message}, \n
            Remetente: {user.id_user}, \n
            id_group: {group.id_group}, \n
            content: {self.content}, \n
            link: {self.link}, \n
            dt_create: {self.dt_create}
            """