from django.db import models

class User(models.Model):


    id_user = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 150)
    office = models.CharField(max_length= 120)
    depth = models.CharField(max_length = 100)
    mail = models.EmailField(max_length = 150)
    phone = models.CharField(max_length = 19)    

    def __str__(self):
        return f"""id_user: {self.id_user},\n 
                    name: {self.name},\n
                    office: {self.office},\n
                    depth: {self.depth},\n
                    mail: {self.mail},\n
                    phone: {self.phone} """ 
    
    

