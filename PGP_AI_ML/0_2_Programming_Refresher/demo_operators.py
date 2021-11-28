'''
Created on 3 Oct. 2021

@author: praka
'''
a,b,c = 10, 20, 23
print("****Arithmetic Operators")
print(a+b)   # Addition
print(b-a)   # Subtraction
print(b*a)   # Multiply
print(b/a)   # Divide
print(c//a)  # Divide and Result is Integer
print(c%a)   # Remainder (Modulus)
print(a**3)  # Power Of

print("****Conditional Operators")
print(a<b)   # Less Than
print(a>b)   # Greater Than
print(a<=b)  # Less Than and Equal To
print(c>=b)  # Greater Than and Equal To
print(a!=b)  # Not Equal To
print(a*2 == b) # Equal To

print("****Is Operator")
d = a 
print(a is d)      # Is Referring to Same Object?
print(a is not c)  # Is Not Referring to Same Object?

print("****In Operator")
e = "Do You know me? Yes or No"
f = "Yes"
g = "Why"
print(f in e, ":'", e, "' contains '", f, "'")         # Contains
print(g not in e, ":'", e, "' not contains '", g, "'") # Not Contains