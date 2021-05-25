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
        hist_grouped = hist.val
        list_id_group = [item["Group"]for item in hist_grouped.values()]
        return {[ {"name": index["name"],"id" : index["id_group"]} for index in list_id_group[:12]]}

    except Exception:
        print("error")
        return {"error": Exception}

def searcher(names):
    try:
        users = User.objects.filter(name__contains = names)
        names = [ {"name": user["name"], "id" : user["id_user"]} for user in users.values()]
        groups = []
        duos = []
        for user_int in users:
            groups = Group.objects.filter(id_user__contains = user_int)
        result = groups
        if len(groups) < 8:
            different = 8  - len(groups)
            try: 
                result.extend(users[:different])
            except:
                pass
        return result
    except Exception:
        return {"error": Exception}