from django.db import models
from .Models.user import (User)
from .Models.group import (Group)
from .Models.connect_user import (Connection)

def valit_user(mail, password ):
    try: 
        user = User.objects.get(mail = mail, password= password)
        return {"id": user.id_user}
    except Exception:
        return {"error": Exception}

def info_user(id_user):
    try: 
        user = User.objects.get(id_user = id_user)
        return {
        "id": user.id_user, 
        "name": user.name,
        "office": user.office,
        "depth": user.depth,
        "mail": user.mail,
        "phone": user.phone}

    except Exception:
        return {"error": Exception}


