
import re   
  
email_redux = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
def validate_email(email):   
  
    if(re.search(email_redux,email)):   
            return True
    else:   
            return False
pass



phone_redux_form1 = '^09[0-9]{9}$'

phone_redux_form2 = '^\+989[0-9]{9}$'

phone_redux_form3 = '^00989[0-9]{9}$'




def validate_phone(phone_number) : 
    if(re.search(phone_redux_form1 , phone_number)):
        return True
    if(re.search(phone_redux_form2 ,phone_number)):
        return True
    if(re.search(phone_redux_form3 , phone_number)):
        return True
    else : 
        return False
pass


my_phone_number = '09121011498'
my_phone_number2 = '+989107895232'
my_phone_number3 = '093311111111'


if(validate_phone(my_phone_number)) : 
    print("its ok ! ")
else : 
    print("invalid ! ")


if(validate_phone(my_phone_number2)) : 
    print("its ok ! ")
else : 
    print("invalid ! ")
    
if(validate_phone(my_phone_number3)) : 
    print("its ok ! ")
else : 
    print("invalid ! ")