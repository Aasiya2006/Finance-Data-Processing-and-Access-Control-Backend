def check_permissions(user_role,action):
    permissions = {
        "viewer" : ["read"],
        "analyst" : ["read","summary"],
        "admin" : ["create","read","update","delete","summary"]
    }
    return action in permissions.get(user_role,[])