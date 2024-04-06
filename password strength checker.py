# Password strength checker program 
import re 
# Password must be at least 8 charcters long
password = input("Enter Your Password: ")
if len(password) < 8:
    print("Password must be at least 8 charcters long")
    # Password must contain at least one uppercase letter
elif not re.search("[A-Z]", password):
    print("Password must contain at least one uppercase letter.")
    # Password must contain at least one lowercase letter
elif not re.search("[a-z]", password):
    print("Password must contain at least one lowercase letter.")  
    # Password must contain at least one number      
elif not re.search("[0-9]", password):
    print("Password must contain at least one number.")
    # Password must contain at least one speacial character
elif not re.search("[~,@,!,#,$,%,&,*,(),_,-,+,=,/,;,:,"",.,{},+]", password):
    print("Password must contain at least one speacial character.")
else:
    print("Password is Strong.")        