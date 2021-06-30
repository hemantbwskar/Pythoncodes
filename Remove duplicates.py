numbers=[2,5,7,9,3,1,26,74,1,2,5]
unique=[]
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)