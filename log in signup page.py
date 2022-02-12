import json
print("welcome to login signup page")

login_signup=input("what is choose login or signup:")
if login_signup=="signup":
     user1=input("enter the user name:")
     fast_name=input("enter your fast name:")
     last_name=input("enter your last name:")
     mobile_number=input("enter the mobile number")
     email=input("enter you email:")
     pass1=input("enter the password:")
     pass2=input("enter the conform password:")
     if pass1==pass2:
          print("your password is correct:")
          birth=input("enter you date of brith:")
          gender=input("choose your gender M/F:")
          print("signup successful")
          dict={"login_signup":login_signup,"email":email,"pass1":pass2,"birth":birth,"gender":gender}
          with open("text.json","w") as f:
               b=json.dump(dict,f,indent=4)
     else:
          print("both password are not same")
else:
     if login_signup=="login":
          user1=input("enter the name:")
          pass1=input("enter the password:")
          with open("text.json","r") as f:
               b=json.load(f)
               print("login successful")
     else:
          print('it is wrong') 
              