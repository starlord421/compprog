fizzbuzz=input("what number do you want to buzz")
for i in range(0,int( fizzbuzz)):
    if i % 3== 0 and i % 5== 0:
        print(f"{i}fizzbuzz")
    elif i % 3==0:
        print(f"{i}fizz")
    elif i % 5==0:
        print(f"{i}buzz")