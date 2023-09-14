first_number= int(input('what number do you want to calculate'))
second_number= int(input('what other number do you want to calculate'))
add= {first_number + second_number}
multiply= {first_number * second_number}
divide= {first_number / second_number}
subtract= {first_number-second_number}

print(f'{first_number}+{second_number} is equal to {add}')
print(f'{first_number}*{second_number} is equal to {multiply}')
print(f'{first_number}/{second_number} is equal to {divide}')
print(f'{first_number}-{second_number} is equal to {subtract}')