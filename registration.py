


userRedux = '^[0-9]+' 
def check_registration_rules(**kwargs):
    for username , password in kwargs.items() :
        if len(username) > 3 and len(password) > 5 and username != "codecup" and username != "quera" :
            pass

