# Author : Harrison Toppen-Ryan
# Description : Lab 3, CSCI 141
# Date : October 14th, 2020

# Ask the user if its sunny
sun = input("Is it sunny?: ")

# if it is sunny outside
if sun == "yes":
     # Asking for the temperture 
    temp = int(input("What is the temperture?: "))
    if temp < 60:
        print("Wear a sweater")
    elif temp == 60:
        print("Woo hoo, it is 60 degrees. Wear what you want")
    #If the temperture is greater then 60 degrees 
    else:
        print("Wear a tee shirt and flip flops")
# If it is not sunny outside 
elif sun == "no":
    #Asking for the temperture 
    temp = int(input("What is the temperture?: "))
    if temp < 40:
        print ("Wear a coat and hat")
    elif temp >= 40 and temp <= 50:
        print("Not quite freezing, but close. Bundle up")
    elif temp == 50:
        print("A jacket is best")
    #If the temperture is greater then 50 degrees 
    else:
        print("Wear a long sleeved shirt")
    

