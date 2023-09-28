print('congrats, the company has deemed that a five year employee is to recive a bonus of 5%')

salary = int(input('what is your salary'))

year = int(input('how long have you been with us'))

if year >= 5: print (salary * 1.05 )
else: print ('you are not qualified')

square_vs_rectangle_length = input('what demention do you want')

square_vs_rectangle_side=input('what is the second demention')

if square_vs_rectangle_side == square_vs_rectangle_length: print ('this is a square')

else: print ('this is a rectangle')

user_input = int(input('what number do you want'))

twoser_input = int(input('what other number do you want'))

if user_input > twoser_input: print(user_input)

else: print(twoser_input)

attendence = int(input('what percentage of class attendence do you have'))

if attendence >= 75: print ('you are free to take the exam')

else: print ('then get out of here')

if attendence > 100: print ('nice try fool, get the frick out of here.')

age_input = int(input('what is the first age'))
age_input2 = int(input('what is the second age'))
age_input3 = int(input('what is the third age'))

if age_input > age_input2 and age_input3: print (f'the first dude is a boomer at {age_input} years old')

if age_input3 > age_input2 and age_input: print (f'the third dude is a boomer at {age_input3} years old')

if age_input2 > age_input and age_input3: print (f'the second dude is a boomer at {age_input2} years old')