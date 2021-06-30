a1=[2,4,3,15,8,19]

a2=[4,9,27,225,47,16,8]

numbers_done = []
validnum = []


def funsquare(a, b):
    i = 0
    while i < len(validnum):
        if validnum[i]['Num'] == a:
            validnum[i]['Square'] = b
            break
        i += 1
    else:
        validnum.append({'Num': number, 'Square': b})


def funcube(a, b):
    i = 0
    while i < len(validnum):
        if validnum[i]['Num'] == a:
            validnum[i]['Cube'] = b
            break
        i += 1
    else:
        validnum.append({'Num': number, 'Cube': b})


for number in a1:
    if number not in numbers_done:
        for A2 in a2:
            if A2 == number * number:
                funsquare(number, A2)
            elif A2 == number * number*number:
                funcube(number, A2)
        numbers_done.append(number)
print(validnum)

