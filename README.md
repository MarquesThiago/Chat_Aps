# Chat_Aps

## Util  to actvate ambients or servers

    file with codice to activate ambiente of development backend or run server of backend 

```bash 

cd .\Chat_Aps

active_py.bat

```

## routes backend 

* locahost/
    * login User
    * received Email and PAssoword
    * return id_user

* locahost/userInfo
    * information of the user
    * received id_user
    * return object json with information of user 

* locahost/search 
    * search user ou group by name
    * receive names
    * return list name group and id group

* locahost/cache
    * last talks of the user 
    * received id_user
    * return last messages of groups  

* message
    * message received
    * received id_group
    * return last messages of group







