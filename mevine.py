#checking if a string is palendrom or not
s="rotor"
b=""

for i in s:
    b = i + b
if (s==b):
        print("its palendrom")
else:
        print("not palendrom")    
