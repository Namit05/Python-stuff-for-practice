#Staff ID Check!
#Role must not be bigger than 5 letters
#No space or digits

role=("admin","staff")
username=input(f"Enter your role :")
if len (username) >5 :
    print("Role cant be bigger than 5 characters")
elif not username.find(" ")==-1 :
    print("Role cant have space! ")
elif not username.isalpha() :
    print ("Role cant have digits!")
elif username not in role :
    print("Invalid role!")
else :
    print(f"Welcome {username}")

    name=input("Enter your Name :").lower()
    if username=="admin" :
        print(f"Welcome Admin {name}")
        if name=="namit" :
            print("Your Clearence level is level 3")
        
        else :
            print("Your Clearence level is level 2")

    while name=="namit" :
        print("What area are you trying to access?")
        print("1.Main Control System")
        print("2.Security System")
        print("3.Operations System")
        print("4.Chemical Facility")

        choice=int(input("Enter a choice 1-4 :"))

        if choice==1 :
            print("You may proceed to the main controls!")
            break
        elif choice==2 :
            print("You may proceed to the security systems!")
            break
        elif choice==3 :
            print("You may proceed to the operation table!")
            break
        elif choice==4 :
            print("You may proceed to the chemical facility!")
            break

        else :
            print("Invalid choice!")

        



        







    









