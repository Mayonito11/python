#slicing
s="python"
print(s[1:4])
import pandas as np
import re
S=input("enter a string:")

if re.fullmatch("[A-Za-z0-9]+",S):
 print("the string contins only letters and digits")
else:
 print("the string contains other characters") 