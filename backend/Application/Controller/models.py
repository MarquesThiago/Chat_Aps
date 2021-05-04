from django.db import models
from .Models.user import (User)
from .Models.group import (Group)
from .Models.connect_user import (Connection)
from .Models.historic import (Historic)
from django.db.models.functions import Lower
from django.db.models import (Max, Count)
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

def historic(id_group):
    try: 
        group = Group.objects.get(pk = id_group)
        hist = Historic.objects.filter(id_group = group).order_by(Lower("dt_create").desc())
        new_hist = []
        for unity in hist[:20]:
            user = unity.id_user
            group = unity.id_group
            message = {
               "id_message": unity.id_message,
               "user": user.id_user,
               "group": group.id_group,
               "message": unity.content,
               "link": unity.link,
               "date": str(unity.dt_create)
           }
            new_hist.append(message)
        return new_hist
    except Exception:
        print("error")
        return {"error": Exception}

def cache_chat(id_user):
    try: 
        user = User.objects.get(pk = id_user)
        groups = Group.objects.filter(id_user = user)

        hist = Historic.objects.filter(id_group__in = groups).order_by(Lower("dt_create").desc())
        hist_grouped = hist.values_list("id_group", "dt_create").aggregate(Group = Max("id_group"),dt_max = Max("dt_create"))
        print(hist_grouped)
        list_id_group = [ item["Group"] for item in hist_grouped.values()]
    
    except Exception:
        print("error")
        return {"error": Exception}

