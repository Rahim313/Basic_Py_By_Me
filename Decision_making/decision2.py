# list creation
'''
username=["lnb","Arked","Rahim","Raju"]
user=input("Enter user name..")

if user in username:
        print("Username is correct..")
        print("welcome",user)
else:
    print(user,"is not present in list")

'''


# to check create username and pass




user_pass={"Arked":"123","Rahim":"456","Ark":"789"}
user1=input("Enter user name : ")
if user1 in user_pass:
    print("Ok user is present")
    pw=input("Enter password : ")
    if pw in user_pass[user1]:
        print("password is correct")
    else:
        print("please enter ocrrect password")
else:
    print("user is not present..")


