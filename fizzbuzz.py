fizzbuzz=input("what number do you want to buzz")
for i in range(0,int(fizzbuzz)):
    if i % 3 != 0 or i % 2 != 0 or i % 5 != 0:
        print("prime")
    if i % 3== 0 and i % 5== 0:
        print("fizzbuzz")
    elif i % 3==0:
        print("fizz")
    elif i % 5==0:
        print("buzz")
    else: print (i)