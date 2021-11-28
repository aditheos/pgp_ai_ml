'''
Created on 3 Oct. 2021

@author: praka
'''
def age(a): 
    if (a > 18): 
        print("You are over 18")
    elif(a == 18): 
        print("You are 18")
    else: 
        print("You are under 18")
    
print("enter your age \n")
a = input()
b = int(a)
age(b)

print("****Ternary If")
print( "Adult" if(b>18) else "Not an Adult")