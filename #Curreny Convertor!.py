#Curreny Convertor!

Currency = input("Choose your desired currency dollar or ruppee (D/R) :")
Money=float(input("enter the amount :"))
if Currency =="R" :
    Money=(Money/87.7 )
    print(f"Here is your money in dollars {Money}")
elif Currency =="D" :
    Money=(Money*87.7 )
    print(f"here is your money in ruppees{Money}")
else :
    print("Sorry! we dont exchange that currency here")