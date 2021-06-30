a1='aabbb'
a2='aabbbaa'
a3='abab'
a4='bbbb'

charb=False
i=0
while i<len(a4):
    print(a4[i])
    if a4[i]=='b':
        charb=True
    if charb==True and a4[i]=='a':
        print('A after B')
        break
    i+=1
else:
    print('No A after B')