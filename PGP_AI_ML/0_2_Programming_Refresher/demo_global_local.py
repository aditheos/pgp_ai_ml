'''
Created on 4 Oct. 2021

@author: praka
'''

x = "Global_X"
print("Global & Local\n")
def local():
    x = "Local_X"
    print(x)

local()
print(x)

print("\nChange Global in Local Scope\n")
def local2():
    global x
    x = "Local_X"
    print(x)

local2()
print(x)