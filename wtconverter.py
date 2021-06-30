weight=int(input('Weight: '))
def wt_converter():
    unit=input('Lbs or Kg: ')
    if unit.lower()=='lbs':
        print(f'Your weight in kg is {weight*0.45}.')
    elif unit.lower()=='kg':
        print(f'Your weight in pounds is {(weight// 0.45)}.')
    else:
        print('Please enter valid unit')
        wt_converter()
wt_converter()
print('Thank you!')