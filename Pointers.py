num1=11
num2=22
print(num1)
print(num2)
print(id(num1)==id(num2))


dict1={'value':11}
dict2=dict1
dict2['value']=22
print(dict1,dict2)
print(id(dict1)==id(dict2))

#pointer are locations of values every 