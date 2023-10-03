user_input=int(input("between 1 and ten for the amount of numbers"))
for i in range (1):
        if user_input== 1:
            print (f'0')
        if user_input==2:
           print(f'0,1')
        if user_input==3:
            print(f'0,1,1')
        if user_input==4:
            print(f'0,1,1,2')
        if user_input==5:
            print(f'0,1,1,2,3')
        if user_input==6:
            print(f'0,1,1,2,3,5')
        if user_input==7:
            print(f'0,1,1,2,3,5,8')
        if user_input==8:
            print(f'0,1,1,2,3,5,8,13')
        if user_input==9:
            print(f'0,1,1,2,3,5,8,13,21')
        if user_input==10:
            print(f'0,1,1,2,3,5,8,13,21,34')
        if user_input > 10:
            print('please use a number that my tiny brain had the intellectual capacity to program')