from django.db import models

class User(models.Model):


    id_user = models.AutoField(primary_key = True, null = False, blank = False)
    name = models.CharField(max_length = 150, null = False, blank = False)
    password = models.CharField(max_length= 20, null = False, blank = False)
    office = models.CharField(max_length= 120, null = False, blank = False)
    depth = models.CharField(max_length = 100, null = False, blank = False)
    mail = models.EmailField(max_length = 150, null = False, blank = False)
    phone = models.CharField(max_length = 19, null = False, blank = False)


    def __str__(self):
        return f"""id_user: {self.id_user},\n 
                    name: {self.name},\n
                    office: {self.office},\n
                    depth: {self.depth},\n
                    mail: {self.mail},\n
                    phone: {self.phone} """ 
    
    

