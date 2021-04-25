from django.db import models
from .user import User

class Connection(models.Model):
    id_connect = models.AutoField(primary_key = True)
    id_user = models.OneToOneField(User, related_name ="pk_id_user", on_delete = models.RESTRICT)
    address = models.CharField(max_length = 150)

    def __str__(self):
        return f"""
            id_connect: {self.id_connect}, \n
            id_user: {self.id_user}, \n
            address: {self.address}
        """