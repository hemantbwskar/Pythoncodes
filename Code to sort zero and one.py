a='0210202102102022'
print(a)

# Method 1
zeros= ''
ones=''
twos=''
for char in a:
    if char=='0':
        zeros+=char
    elif char=='1':
        ones+=char
    else:
        twos+=char
a1=zeros+ones+twos

print(a1)



#method 2

# a1=[0,1,0,0,1,0,1,0,0,1,0,1,0,1,1,1,0,0]
# a2=[]
# for element in a:
#     if element=='0':
#         a2.insert(0,element)
#     else:
#         a2.append(element)
#
# print(a2)