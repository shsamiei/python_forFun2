import re
passRedux = '^[0-9]+$' 
def check_registration_rules(**kwargs):
    validateList = []
    for username , password in kwargs.items() : 

        if len(username) > 3 and len(password) > 5 :
            if(username != "codecup" and username != "quera") :
                if  not(re.search(passRedux ,password)):
                    validateList.append(username)
                    
    return validateList





                

dict = {'alii': '1123313' , 'hossein' : '234#erkjf3' , 'mmohadese' : '09238833' , 'yekta' : '892e247'}
print(check_registration_rules(**dict))



  




    
