#Compound Interest Calculator

principle=0
rate=0
time=0

while True :
    principle=float(input("Enter the desired amount! :"))
    if principle < 0:
        print("principle cant be less than zero ! ")
    else : 
        break
    
     

while True :
    rate=float(input("Enter the rate amount! :"))
    if rate < 0:
        print("Interest rate cant be less than zero ! ")
    else : 
        break
    
while True  :
    time=float(input("enter the time! :"))
    if time <0 :
        print("time cant be less than zero ! ")
    else : 
        break

total= principle* pow((1+rate/100), time)
print (f"Balance after {time} year/s : ${total}.2f")

