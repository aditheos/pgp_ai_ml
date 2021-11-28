'''
Created on 3 Oct. 2021

@author: praka
'''
a = 0
print("While Loop \n")
while a < 10:
    a = a + 1
    if (a == 1):
        print("The (WHILE) iteration# is " + str( a ))
    else:
        continue
    
    if( a == 2): 
        break 
    
print("\n")

print("For Loop \n")
a = 0
for a in range(0,10):
    if( a > 1 ):
        print("The (FOR) iteration# is " + str( a + 1 ))
    else:
        continue
    if( a == 3): break
    
print("\n")